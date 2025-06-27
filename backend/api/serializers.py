import logging
import requests
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.core.cache import cache
from django.conf import settings
from rest_framework import serializers


logger = logging.getLogger(__name__)


def check_captcha(captcha):
    if not captcha or captcha.strip() == '':
        raise serializers.ValidationError({"captcha_error": "Captcha is required."})
    
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': captcha,
    }

    try:
        response = requests.post(url, data=data, timeout=5)
        result = response.json()
        logger.warning(f"Captcha Validation: {result}")
        if not result.get('success', False):
            raise serializers.ValidationError({"captcha_error": "Captcha is invalid. Please try again."})

    except requests.RequestException:
        raise serializers.ValidationError({"captcha_error": "Captcha verification failed. Please try again."})


class RegisterUser(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    captcha = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'captcha']

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already in use.")
        return email

    def validate(self, attrs):
        check_captcha(attrs.get('captcha'))
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Password does not match."})
        validate_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data.pop('captcha')
        return User.objects.create_user(**validated_data)


class LoginUser(serializers.Serializer):
    username_email = serializers.CharField()
    password = serializers.CharField()
    captcha = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        username_email = attrs.get('username_email').strip()
        password = attrs.get('password')
        captcha = attrs.get('captcha')

        key = f'failed_login:{username_email}'

        login_attempts = cache.get(key, 0)
        
        if login_attempts >= 3:
            check_captcha(captcha)

        user = authenticate(username=username_email, password=password)

        if not user:
            login_attempts += 1
            cache.set(key, login_attempts, timeout=900) # 900 is equivalent to 15 minutes reset time
            raise serializers.ValidationError({
                "username_email": "Invalid username or password.",
                "password": "Invalid username or password."
            })

        cache.delete(key)
        attrs['user'] = user
        return attrs

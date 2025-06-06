from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class RegisterUser(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already in use.")
        return email

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Password does not match.')
        validate_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password') # this removed the confirm_password
        return User.objects.create_user(**validated_data)
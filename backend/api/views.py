from .serializers import RegisterUser, LoginUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import PermissionDenied as DjangoPermissionDenied
from rest_framework.exceptions import ValidationError


@api_view(['POST'])
def register_user(request):
    serializer = RegisterUser(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'success': True}, status=201)
    
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_user(request):
    serializer = LoginUser(data=request.data)

    serializer.is_valid(raise_exception=False)

    if serializer.errors:
        errors = serializer.errors.copy()

        captcha_errors = errors.get('captcha_error', [])
        if any("Captcha is required" in err for err in captcha_errors):
            errors['require_captcha'] = True

        return Response(errors, status=400)

    # Auth success
    user = serializer.validated_data['user']
    refresh = RefreshToken.for_user(user=user)
    access = refresh.access_token

    return Response({
        'success': True,
        'refresh': str(refresh),
        'access': str(access),
        'username': user.username,
    }, status=200)

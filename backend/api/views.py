from .serializers import RegisterUser, LoginUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django_ratelimit.decorators import ratelimit
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
@ratelimit(key='ip', rate='5/m', method='POST', block=False)
@ratelimit(key='post:username_email', rate='5/m', method='POST', block=False)
def login_user(request):

    if getattr(request, 'limited', False):
        raise DjangoPermissionDenied("Too many attempts.")
    
    try:
        serializer = LoginUser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user=user)
            access = refresh.access_token
            return Response({
                'success': True, 
                'refresh': str(refresh),
                'access': str(access),
                'username': user.username,
            }, status=200)
    except DjangoPermissionDenied:
        return Response(
            {'error': 'Too many login attempts. Please try again in a few minutes.'},
            status=403
        )
    except ValidationError as ve:
        return Response({'error': ve.detail.get('non_field_errors', ['Invalid credentials.'])[0]}, status=401)
    except Exception:
        return Response({'error': 'Something went wrong on the server.'}, status=500)

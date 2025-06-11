from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import register_user, login_user

urlpatterns = [
    path('api/register/', register_user, name='register'),
    path('api/login/', login_user, name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
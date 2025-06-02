from django.urls import path
from .views import product_detail

urlpatterns = [
    path("products/<int:pk>/", product_detail),
]

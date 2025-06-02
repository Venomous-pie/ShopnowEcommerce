from django.contrib import admin
from django.urls import path, include
from api.views import product_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("products/<int:pk>/", product_detail),
]

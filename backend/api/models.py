from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True, null=True)
    additional_img = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    discount_percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# TODO: 
class Cart(models.Model):
    pass

class Wishlist(models.Model):
    pass

class Order(models.Model):
    pass
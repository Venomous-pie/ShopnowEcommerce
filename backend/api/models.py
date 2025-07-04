from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Attribute(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    class Meta:
        unique_together = ('attribute', 'value')

    def __str__(self):
        return f'{self.attribute.name}: {self.value}' 


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=300, unique=True)

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=400)

    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    STOCK_STATUS = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('low_stock', 'Low Stock'),
        ('pre_order', 'Pre-Order'),
    ]

    stock = models.PositiveIntegerField(default=0)
    stock_status = models.CharField(
        max_length=20,
        choices=STOCK_STATUS,
        default='in_stock'
    )

    image = models.URLField(blank=True, null=True)
    #additional_img = models.JSONField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_number = models.CharField(max_length=100)
    
    weight = models.DecimalField(max_digits=10, decimal_places=2) # kg
    dimension = models.CharField(max_length=50)
    free_shipping = models.BooleanField(default=False)
    ship_from = models.CharField(max_length=500)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    review_count = models.PositiveIntegerField(default=0)
    country_of_origin = models.CharField(max_length=100)
    province_of_origin = models.CharField(max_length=100)

    hazardous_material = models.BooleanField(default=False)
    hazardous_regulations = models.TextField(blank=True)
    age_restrictions = models.CharField(max_length=20, default='None')

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    attributes = models.ManyToManyField(AttributeValue, related_name='variant_attribute')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return f'{self.sku} - {self.price}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveBigIntegerField(default=0)
    comment = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
    

# TODO: 
class Cart(models.Model):
    pass

class Wishlist(models.Model):
    pass

class Order(models.Model):
    pass
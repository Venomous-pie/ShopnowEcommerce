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
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variants')
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
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user',)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product_variant.price * self.quantity

    def __str__(self):
        return f'{self.cart.user.username} - {self.product_variant.sku} * {self.quantity}'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username}: {self.product.product.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user',)

    def __str__(self):
        return f'Order: {self.user.username}'
    
    @property
    def total_price(self):
        return sum(item.total_price() for item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)

    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    is_default = models.BooleanField(default=False)
    is_billing = models.BooleanField(default=False)
    is_shipping = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s Address'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
from django.db import models
from django.contrib.auth.models import User

class Order (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True) # Creacion de la fecha automaticamente

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"order {self.id} by {self.user.username}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Order(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.usuario.username}"
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"
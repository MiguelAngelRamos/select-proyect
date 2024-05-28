from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('shipping', 'Shipping'),
        ('delivered', 'Delivered'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    order_number = models.CharField(max_length=10, unique=True)
    delivery_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return self.order_number
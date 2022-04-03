from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2)

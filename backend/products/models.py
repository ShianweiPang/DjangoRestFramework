from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        # do alot complicated calculation here
        return "12.44"
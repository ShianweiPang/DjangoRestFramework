from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "brand",
            "content",
            "price",
            "sale_price",
            "get_discount",
        ]

    def get_my_discount(self, obj):
        try:
            return self.get_discount()
        except:
            return None
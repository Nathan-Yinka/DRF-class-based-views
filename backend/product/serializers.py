from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["sale_price","title","content","price","id","my_discount"]
    
    def get_my_discount(self,obj):
        return obj.get_discount()
from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title,unique_product_title,validate_title_no_hello
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk")
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello,unique_product_title])
    name = serializers.CharField(source="title",read_only=True)
    class Meta:
        model = Product
        fields = ["id","url","edit_url","sale_price","email","title","content","price","my_discount","name","user"]
    
    def get_my_discount(self,obj):
        return obj.get_discount()
    
    # def validate_title(self,value):
    #     qs = Product.objects.filter(title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product title")
    #     return value
    
    def get_edit_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.id},request=request)
        
    def create(self, validated_data):
        email = validated_data.pop("email")
        return super().create(validated_data)
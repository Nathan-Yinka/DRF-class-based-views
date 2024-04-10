from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product
from product.serializers import ProductSerializer

# Create your views here.

@api_view(["GET","POST"])
def api_home(request,*args, **kwargs):
    """
    DRF API View
    """
    serializer ={}
    products = Product.objects.all().order_by("?").first()
    if products:
        serializer = ProductSerializer(products).data
    return Response(serializer)
    
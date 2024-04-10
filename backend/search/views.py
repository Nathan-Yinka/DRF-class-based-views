from django.shortcuts import render
from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer

# Create your views here.

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            qs = qs.search(q,user)
        
            return qs
        return qs.none()
        
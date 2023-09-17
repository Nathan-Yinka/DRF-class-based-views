from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from api.mixin import StaffEditorPermissionMixin
from api.authentication import TokenAuthentication
from api.permission import IsStaffEditorPermission

class ProductRetrieveUpdateDestroyAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field= "pk"   #the fields we going to reteieve the objext instance
    
class ProductListCreateAPIView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        
        if content is None:
            content = title
        print(content)
        serializer.save(content=content)


# class ProductMixinView(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def get(self,request,*args,**kwargs):
#         pk = kwargs.get("pk",None)
#         if pk is not None:
#             return self.retrieve(request,*args, **kwargs)
#         return self.list(request,*args, **kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)
    
#     def perform_create(self, serializer):
#         title = serializer.validated_data.get("title")
#         content = serializer.validated_data.get("content") or None
        
#         if content is None:
#             content = title
#         print(content)
#         serializer.save(content=content)
    
#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)
    
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)
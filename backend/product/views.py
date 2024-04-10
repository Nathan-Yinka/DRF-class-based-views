from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from api.mixin import StaffEditorPermissionMixin,UserQueryMixin
from api.authentication import TokenAuthentication
from api.permission import IsStaffEditorPermission

class ProductDestroyAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()
    
class ProductListCreateAPIView(StaffEditorPermissionMixin,UserQueryMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view = False
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        
        if content is None:
            content = title

        serializer.save(content=content,user=self.request.user)
    
    # def get_queryset(self,*args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     if not self.request.user.is_authenticated:
    #         return Product.objects.none
    #     return qs.filter(user=self.request.user)
    
        
product_list_create_view = ProductListCreateAPIView.as_view()
        
        
class ProductDetailAPIView(StaffEditorPermissionMixin,UserQueryMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()









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
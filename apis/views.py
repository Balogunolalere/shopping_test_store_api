from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .serializers import ProductSerializer, CategorySerializer

from stores.models import Product, Category

from .permissions import IsOwnerOrReadOnly




class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
        
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    

    

from django.urls import path

from .views import ProductCreateAPIView, ProductRetrieveUpdateDestroyAPIView, ProductListAPIView,CategoryListAPIView


urlpatterns = [
    path('', ProductListAPIView.as_view(), name='Product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='create-product'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
        
]

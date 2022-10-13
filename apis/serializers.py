from rest_framework import serializers

from stores.models import Product, Category



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ['date_created', 'date_updated']
        extra_kwargs = {'owner': {'read_only': True}}
        fields = ('id', 'name', 'description', 'date_created', 'date_updated', 'size','price', 'tags', 'owner', 'category')
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
        
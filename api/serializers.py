from rest_framework import serializers
from shop.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, source='category')

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'price', 'product_qty', 'category', 'category_id', 'created_at', 'image']
        read_only_fields = ['slug', 'created_at']
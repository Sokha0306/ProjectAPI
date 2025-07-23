from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:        
        model =  Product
        fields = ['id', 'productName', 'categoryID','price','productDescript', 'weight', 'availability', 'shipping', 'productImage']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:        
        model =  Category
        fields = ['id', 'categoryName', 'categoryImage']
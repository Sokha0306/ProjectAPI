from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:        
        model =  ProductList
        fields = ['id', 'ProLName', 'ProCategoryID','ProLPrice', 'ProLImage']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:        
        model =  ProductCategory
        fields = ['id', 'CategoryName']
from rest_framework import serializers
from .models import Category, Favourite

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'description', 
            'created', 'modified']


class FavouriteOutputSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Favourite
        fields = [
            'id', 'title', 'description', 
            'rank', 'meta', 'category', 
            'created', 'modified']

class FavouriteInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = [
            'id', 'title', 'description', 
            'rank', 'meta', 'category', 
            'created', 'modified'
        ]
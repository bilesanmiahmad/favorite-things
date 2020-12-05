from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .models import Category, Favourite
from .serializers import CategorySerializer, FavouriteOutputSerializer, FavouriteInputSerializer

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer


class FavouriteViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteInputSerializer

    @action(methods=['GET'], detail=False, url_path='get-favourites')
    def get_favourites(self, request):
        favourites = Favourite.objects.order_by('id')
        serializer = FavouriteOutputSerializer(favourites, many=True)
        return Response(
            {
                'results': serializer.data,
            },            
            status=status.HTTP_200_OK
        )
from django.shortcuts import render
from rest_framework import permissions, viewsets, filters
from rest_framework.pagination import PageNumberPagination


from .models import Titles, Genres, Categories
from .serializers import GenreSerializer, CategoriesSerializer, TitlesSerializer
from .permissions import IsOwnerOrReadOnly



class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all() 
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    http_method_names = ['get', 'post', 'del'] 

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all() 
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          )

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all() 
    serializer_class = TitlesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly,)
    pagination_class = PageNumberPagination

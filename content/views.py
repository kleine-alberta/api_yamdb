from django.shortcuts import render
from rest_framework import permissions, viewsets, filters


from .models import Titles, Genres, Categories
from .serializers import GenreSerializer, CategoriesSerializer, TitlesSerializer



class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all() 
    serializer_class = GenreSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all() 
    serializer_class = CategoriesSerializer

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all() 
    serializer_class = TitlesSerializer

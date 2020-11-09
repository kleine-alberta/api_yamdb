from django.shortcuts import render
from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Titles, Genres, Categories
from django.contrib.auth import get_user_model
from .serializers import GenreSerializer, CategoriesSerializer,  TitlesSerializerGet, TitlesSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly, IsSuperuserPermission
from .filters import TitleFilter

User = get_user_model()


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all() 
    serializer_class = GenreSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter] 
    search_fields = ['=name']
    http_method_names = ['get', 'post', 'delete']

            


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all() 
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    filter_backends = [filters.SearchFilter] 
    search_fields = ['=name']
    http_method_names = ['get', 'post', 'delete']

    

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all() 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    #filter_backends = [filters.SearchFilter] 
    #search_fields = ['=genre__slug', '=category__slug']
    filter_backends = [DjangoFilterBackend] 
    filterset_class = TitleFilter


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitlesSerializerGet
        else:
            return TitlesSerializer

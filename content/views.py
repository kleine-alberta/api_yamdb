from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .filters import TitleFilter
from .models import Categories, Genres, Titles
from .permissions import IsOwnerOrReadOnly, IsSuperuserPermission
from .serializers import (CategoriesSerializer, GenreSerializer,
                          TitlesSerializer, TitlesSerializerGet)

User = get_user_model()


class GenresViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Genres.objects.all() 
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter] 
    search_fields = ['=name']
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']

    def get_permissions(self):
        if (self.request.method != 'GET'):
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]        


class CategoriesViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Categories.objects.all() 
    serializer_class = CategoriesSerializer
    filter_backends = [filters.SearchFilter] 
    search_fields = ['=name']
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'slug'

    def get_permissions(self):
        if (self.request.method != 'GET'):
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes] 


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all() 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend] 
    filterset_class = TitleFilter


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitlesSerializerGet
        else:
            return TitlesSerializer

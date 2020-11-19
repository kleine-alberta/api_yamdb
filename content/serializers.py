from django.db.models import Avg
from rest_framework import serializers

from .models import Categories, Genres, Titles


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['id']
        model = Genres


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['id']
        model = Categories


class TitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Categories.objects.all())
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Genres.objects.all(),
                                         many=True)

    class Meta:
        fields = '__all__'
        model = Titles


class TitlesSerializerGet(serializers.ModelSerializer):
    category = CategoriesSerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.IntegerField()

    class Meta:
        fields = '__all__'
        model = Titles

from rest_framework import serializers

from .models import Genres, Categories, Titles

class GenreSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True
    )

    class Meta:
        fields = "__all__"
        model = Genres

class CategoriesSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all())

    class Meta:
        fields = "__all__"
        model = Categories

class TitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', read_only=True)
    genre = serializers.SlugRelatedField(
        slug_field='slug', read_only=True, many=True)

    class Meta:
        fields = "__all__"
        model = Titles
    

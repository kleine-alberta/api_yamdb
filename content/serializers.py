from rest_framework import serializers

from .models import Genres, Categories, Titles

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Genres


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Categories


class TitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', 
                                            queryset=Categories.objects.all())
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Genres.objects.all(),
                                         many=True)

    class Meta:
        fields = "__all__"
        model = Titles


class TitlesSerializerGet(serializers.ModelSerializer):
    category = CategoriesSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Titles

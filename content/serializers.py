from django.db.models import Avg
from rest_framework import serializers

from .models import Categories, Genres, Titles


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
    rating = serializers.SerializerMethodField()

    def get_rating(self, value):
        queryset = Titles.objects.annotate(rating=Avg('reviews__score')) 
        rating = queryset.get(id=value.id).rating 
        if not rating: 
            return None 
        return round(rating, 1)


    class Meta:
        fields = ['id', 'name', 'year', 'description', 'genre', 'category', 'rating']
        model = Titles

from rest_framework import serializers

from .models import Genres, Categories, Titles

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Genres

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Categories

class TitlesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Titles

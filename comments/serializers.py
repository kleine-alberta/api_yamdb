from django.contrib.auth import get_user_model
from rest_framework import serializers

from content.models import Titles

from .models import Comments, Reviews

User = get_user_model()


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    def validate_title(self, value):
        raise serializers.ValidationError(value)

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        read_only_fields = ('title',)
        model = Reviews


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')


    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        read_only_fields = ('review',)
        model = Comments
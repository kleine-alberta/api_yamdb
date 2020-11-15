from django.shortcuts import get_object_or_404, render
from rest_framework import filters, permissions, serializers, viewsets
from rest_framework.pagination import PageNumberPagination

from content.models import Titles

from .models import Comments, Reviews
from .permissions import IsAuthorOrAdminOrModerator
from .serializers import CommentsSerializer, ReviewsSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrAdminOrModerator]
      
    def get_queryset(self):
        title = get_object_or_404(Titles, id=self.kwargs['title_id'])
        return title.reviews.all()
        

    def perform_create(self, serializers):
        title = get_object_or_404(Titles, id=self.kwargs['title_id'])
        if Reviews.objects.filter(author=self.request.user, title=title):
            raise serializers.validate_title("Нельзя оставлять больше одного отзыва!")
        serializers.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrAdminOrModerator]

    def get_queryset(self):
        review = get_object_or_404(Reviews, id=self.kwargs['review_id'])
        return review.comments.all()

    def perform_create(self, serializers):
        review = get_object_or_404(Reviews, id=self.kwargs['review_id'])
        serializers.save(author=self.request.user, review=review)

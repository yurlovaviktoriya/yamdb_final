from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api_titles.models import Title
from api_users.models import CustomUser

from .models import Review
from .serializers import CommentSerializer, ReviewSerializer
from api_yamdb.permissions import (ReadOnlySafeMethods,
                                   IsOwner,
                                   IsAdminOrStaff,
                                   IsModerator)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        ReadOnlySafeMethods | IsAuthenticated,
        ReadOnlySafeMethods | IsOwner | IsAdminOrStaff | IsModerator
    )

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        author = get_object_or_404(CustomUser, pk=self.request.user.id)
        serializer.save(author=author, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        ReadOnlySafeMethods | IsAuthenticated,
        ReadOnlySafeMethods | IsOwner | IsAdminOrStaff | IsModerator
    )

    def get_queryset(self):
        review = get_object_or_404(Review,
                                   pk=self.kwargs.get('review_id'),
                                   title=self.kwargs.get('title_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review,
                                   pk=self.kwargs.get('review_id'),
                                   title=self.kwargs.get('title_id'))
        author = get_object_or_404(CustomUser, pk=self.request.user.id)
        serializer.save(author=author, review=review)

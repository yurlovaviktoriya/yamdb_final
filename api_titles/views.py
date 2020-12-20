import django_filters
from django.db.models import Avg
from rest_framework import filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_titles.filters import TitleFilter
from api_titles.models import Category, Genre, Title
from api_titles.serializers import (CategorySerializer,
                                    GenreSerializer,
                                    TitleShowSerializer,
                                    TitleWriteSerializer)
from api_yamdb.permissions import (ReadOnlySafeMethods,
                                   IsAdminOrStaff)


class BaseListCreateDestroyView(ModelViewSet):
    permission_classes = (IsAdminOrStaff | ReadOnlySafeMethods,)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name', )
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perfom_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoryListCreateDestroy(BaseListCreateDestroyView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreListCreateDestroy(BaseListCreateDestroyView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleModelViewset(ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    permission_classes = (IsAdminOrStaff | ReadOnlySafeMethods,)
    pagination_class = PageNumberPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = TitleFilter
    http_method_names = ('get', 'head', 'options', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleShowSerializer
        return TitleWriteSerializer

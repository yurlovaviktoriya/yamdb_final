from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_titles.views import (CategoryListCreateDestroy,
                              GenreListCreateDestroy, TitleModelViewset)

router_v1 = DefaultRouter()
router_v1.register(
    r'categories',
    CategoryListCreateDestroy,
    basename='categories'
)
router_v1.register(
    r'genres',
    GenreListCreateDestroy,
    basename='genres'
)
router_v1.register(
    r'titles',
    TitleModelViewset,
    basename='titles'
)
urlpatterns = [
    path('v1/', include(router_v1.urls)),
]

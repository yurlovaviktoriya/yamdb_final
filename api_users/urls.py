from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api_users.views import EmailValidView, JwtGetView, UsernameView

api_router = DefaultRouter()
api_router.register(
    r'users',
    UsernameView,
    basename='customuser'
)

auth_path = [
    path('email/',
         EmailValidView.as_view()),

    path('token/',
         JwtGetView.as_view()),
]

token_path = [
    path('',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh')
]

user_path = [
    path('', include(api_router.urls)),

    path('auth/', include(auth_path)),

    path('token/', include(token_path))
]

urlpatterns = [
    path('v1/', include(user_path))
]
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

api_urls = [
    path('', include('api_users.urls')),
    path('', include('api_titles.urls')),
    path('', include('api_reviews.urls')),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'), name='redoc'),
]

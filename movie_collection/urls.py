from movie_collection import movie_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('collections.urls')),
    path('request-count/', movie_views.RequestCountView.as_view(), name='request-count'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie_collection.urls')),  # Include the app's URL configuration
    path('', include('movie_collection.movie_views')),  # Include the app's views if needed
    path('api-auth/', include('rest_framework.urls')),
]

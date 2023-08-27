from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie_collection.urls')),
    path('', include('movie_collection.movie_views')),  
    path('api-auth/', include('rest_framework.urls')),
]

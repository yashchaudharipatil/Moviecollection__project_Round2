import os
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializers import CollectionSerializer, MovieSerializer, UserSerializer
from rest_framework import permissions
from rest_framework import generics
from .models import Collection
class MovieListView(APIView):
    def get(self, request):
        try:
            # Fetch data from the third-party movie API
            url = "https://demo.credy.in/api/v1/maya/movies/"
            response = requests.get(url, auth=(os.environ.get("MOVIE_API_USERNAME"), os.environ.get("MOVIE_API_PASSWORD")))
            
            if response.status_code == 200:
                movie_data = response.json()
                return Response(movie_data)
            else:
                return Response({"error": "Failed to fetch movie data from the API"}, status=response.status_code)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class CollectionListCreateView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_count = 0

    def __call__(self, request):
        self.request_count += 1
        response = self.get_response(request)
        response['HTTP_X_REQUEST_COUNT'] = str(self.request_count)  # Set the count in the response header
        return response

class RequestCountView(APIView):
    def get(self, request):
        return Response({"requests": request.META.get('HTTP_X_REQUEST_COUNT', 0)})

    def post(self, request):
        request.META['HTTP_X_REQUEST_COUNT'] = 0
        return Response({"message": "request count reset successfully"})

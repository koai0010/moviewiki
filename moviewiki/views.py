from django.shortcuts import render
from rest_framework import viewsets, permissions
from moviewiki.serializer import MovieSerializer, GenreSerializer, PosterSerializer
from moviewiki.models import (
    Movie,
    Genre,
    Poster
)

def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    context = {
        "movies": serializer.data
    }
    return render(request, 'movielanding.html', context)

class MovieViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PosterViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

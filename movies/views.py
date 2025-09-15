from django.shortcuts import render
from rest_framework import generics
from movies.models import Movies
from movies.serializers import MoviesSerializer

class MoviesCreateListAPIView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer







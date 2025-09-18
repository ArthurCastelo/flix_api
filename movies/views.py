from django.shortcuts import render
from rest_framework import generics
from movies.models import Movies
from movies.serializers import MoviesSerializer
from rest_framework.permissions import IsAuthenticated


class MoviesCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer







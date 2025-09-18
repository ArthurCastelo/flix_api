
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated



class GenreListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer











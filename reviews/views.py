from django.shortcuts import render
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated



class ReviewsListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    

class ReviewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer





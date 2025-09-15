from . import views
from django.urls import path

urlpatterns = [
    path('reviews/',  views.ReviewsListCreateAPIView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>',  views.ReviewsRetrieveUpdateDestroyAPIView.as_view(), name='reviews-detail-list')
]
from . import views
from django.urls import path

urlpatterns = [
    path('genres/',  views.GenreListCreateAPIView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>',  views.GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail-list')

]
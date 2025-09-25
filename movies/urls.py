from . import views
from django.urls import path

urlpatterns = [
    path('movies/',  views.MoviesCreateListAPIView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>',  views.MoviesRetrieveUpdateDestroyAPIView.as_view(), name='movies-detail-list'),
    path('movies/stats/', views.MovieStatsView.as_view(),name='stasts-movies',)
]
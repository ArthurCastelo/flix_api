
from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateAPIView,GenreRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',GenreListCreateAPIView.as_view(),name='genre-create-list'),
    path('genres/<int:pk>',GenreRetrieveUpdateDestroyAPIView.as_view(),name='genre-detail-view')
]

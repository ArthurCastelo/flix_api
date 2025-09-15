from . import views
from django.urls import path

urlpatterns = [
    path('actors/',views.ActorListCreateAPIView.as_view(),name='actor-create-list'),
    path('actors/<int:pk>',views.ActorRetrieveUpdateDestroyAPIView.as_view(),name='actor-detail-view')  
]
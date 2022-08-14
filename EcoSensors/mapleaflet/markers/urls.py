"""Markers urls."""

from django.urls import path
from . import views

from .views import MarkersMapView

app_name = "markers"

urlpatterns = [
    path("map/", MarkersMapView.as_view()),
    #path('', views.index, name='index'),
]


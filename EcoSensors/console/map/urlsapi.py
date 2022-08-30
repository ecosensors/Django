from django.urls import path
from . import viewsapi
from map.viewsets import MarkerViewSet

app_name="map"
urlpatterns = [
    path("field/<int:idfield>/", MarkerViewSet.as_view({'get': 'list'}), name="marker_view_set"), # Work with Django Rest Framework
    path('sensor/<int:idsensor>/', viewsapi.sensor, name='apiSensor'), # Api classic a Django

    #path('type/<int:idtype>/', views.api, name='api'),
    #path('station/<int:idstation>/', views.api, name='api'),
]
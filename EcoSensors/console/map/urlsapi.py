from django.urls import path
from . import viewsapi
from map.viewsets import MarkerViewSet,SensorViewSet

app_name="map"
urlpatterns = [
    path("field/<int:idfield>/", MarkerViewSet.as_view({'get': 'list'}), name="marker_view_set"), # Work with Django Rest Framework
    # Old version 1
    #path('sensor/<int:idsensor>/', viewsapi.sensor, name='apiSensor'),
    # New version 1
    path("sensor/<int:idsensor>/", SensorViewSet.as_view({'get': 'list'}), name="sensor_view_set"),
    #try
    #path('sensor/type/<int:idtype>/', viewsapi.type, name='apiType'),

    #path('type/<int:idtype>/', views.api, name='api'),
    #path('station/<int:idstation>/', views.api, name='api'),
]
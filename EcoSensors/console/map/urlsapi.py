from django.urls import path
from . import viewsapi
from map.viewsets import MarkerViewSet, SensorViewSet, TypeViewSet, TestTokenViewSet
"""
    urlpatterns for the API
"""
app_name="map"
urlpatterns = [
    path("field/<int:idfield>/", MarkerViewSet.as_view({'get': 'list'}), name="marker_view_set"), # Work with Django Rest Framework
    # Old version 1
    # path('sensor/<int:idsensor>/', viewsapi.sensor, name='apiSensor'),
    # New version 1
    path("sensor/<int:idsensor>/", SensorViewSet.as_view({'get': 'list'}), name="sensor_view_set"),
    # get the sensors values according to a type
    path("field/<int:idfield>/type/<int:idtype>/", TypeViewSet.as_view({'get': 'list'}), name="type_view_set"),
    # Exercise with Token to protect an API
    path("testToken/<int:idsensor>/", TestTokenViewSet.as_view({'get': 'list'}), name="testToken_view_set"),

    # TODO: Create an api to retrive all measures accordinf to the type of sensors
    #path('sensor/type/<int:idtype>/', viewsapi.type, name='apiType'),
]
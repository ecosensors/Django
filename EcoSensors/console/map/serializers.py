"""Markers serializers."""

"""
# FIRST EXERCISE
from rest_framework import routers,serializers,viewsets
from .models import Stations

class StationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id_station', 'station_name', 'station_longname', 'station_lat', 'station_lng']
        model = Stations
"""
"""
Following the tuto https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/#adding-the-marker-serializer
"""

from rest_framework_gis import serializers

from .models import Stations

class StationsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id_station", "station_name", "station_lat", "station_lng")
        geo_field = "location"
        model = Stations

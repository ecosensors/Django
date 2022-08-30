"""Markers serializers."""

"""
 Maps with Django (2)
 https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/
"""

from rest_framework_gis import serializers
from rest_framework import serializers as ser
from .models import Stations, Measures, Sensors


class StationsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id_station", "station_name", "station_longname", "station_lat", "station_lng", "fields_id_field")
        geo_field = "location"
        model = Stations


class SensorsSerializer(ser.ModelSerializer):
    class Meta:
        fields = ("id_sensor","sensor_name")
        model = Sensors


class MeasuresSerializer(ser.ModelSerializer):
    """
    sensor_name = ser.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='id_sensor'
    )
    """

    sensor_name=SensorsSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        fields = ("sensor_name", "sensor_name", "id_measure","sensors_id_sensor", "value", "measure_created")
        model = Measures


"""
# Previous Exercise
from rest_framework import routers,serializers,viewsets
from .models import Stations

class StationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id_station', 'station_name', 'station_longname', 'station_lat', 'station_lng']
        model = Stations
"""
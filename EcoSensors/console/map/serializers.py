
"""Markers serializers."""
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

"""
 Maps with Django (2)
 https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/
"""

from rest_framework_gis import serializers
from rest_framework import serializers as ser
from .models import Stations, Measures, Sensors, SensorTypes


class StationsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id_station", "station_name", "station_longname", "station_lat", "station_lng", "fields_id_field")
        geo_field = "location"
        model = Stations


class StSerializer(ser.ModelSerializer):
    class Meta:
        fields = ("id_station", "station_longname", "fields_id_field")

        model = Stations

class SensorsSerializer(ser.ModelSerializer):

    stations_id_station = StSerializer(
        read_only=True
    )

    class Meta:
        fields = ("id_sensor","sensor_name", "sensor_longname", "sensor_types_id_sensor_type","stations_id_station")
        model = Sensors


class MeasuresSerializer(ser.ModelSerializer):

    sensors_id_sensor=SensorsSerializer(
        read_only=True
    )

    class Meta:
        fields = ("id_measure", "value", "measure_created", "sensors_id_sensor", "collections_id_collection")
        model = Measures


"""
Keep an yes on the lines bellow (keep it or not), because it is not used anymore
"""
class SensorTypeSerializer(ser.ModelSerializer):
    class Meta:
        fields = ("id_sensor_type","sensor_type_name","sensor_type_longname","measure_unit")
        model = SensorTypes


class TypesSerializer(ser.ModelSerializer):

    sensor_types_id_sensor_type=SensorTypeSerializer(
        read_only=True
    )

    #"sensor_type_name", "measure_unit",
    class Meta:
        fields = ("id_sensor","sensor_name","sensor_types_id_sensor_type")
        model = Sensors


"""
TOKEN
"""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token




"""
# NOTES

## Previous Exercise
from rest_framework import routers,serializers,viewsets
from .models import Stations

class StationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id_station', 'station_name', 'station_longname', 'station_lat', 'station_lng']
        model = Stations
"""
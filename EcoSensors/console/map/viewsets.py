"""
Django © 2022 by Pierre Amey is licensed under CC BY-NC-SA 4.0
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND
"""
from django.db.models import Prefetch

"""Markers API views."""
# Maps with Django (2)
# https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/
#import self
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_gis import filters
from datetime import datetime, timedelta
from rest_framework_simplejwt.views import TokenObtainPairView

from map.models import Stations, Measures, SensorTypes, Sensors
from map.serializers import StationsSerializer, MeasuresSerializer, TypesSerializer, MyTokenObtainPairSerializer

from django.core import serializers
from django.http import HttpResponse

class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API: Return the marker of the positions of the stations. The API is called from map.js
    See project/urlsapi.py (path("api/map/<int:idfield>/", MarkerViewSet.as_view({'get':'list'}), name="marker_view_set"))
    """
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    # See serializers.py
    serializer_class = StationsSerializer

    def get_queryset(self):
        idf = self.kwargs['idfield']
        # if the stations can be showed in the map (map is 1)
        if idf > 0:
            # return the marker of the stations according to the ID of a field
            return Stations.objects.filter(station_active=1, map=1, fields_id_field=idf)
        else:
            # return all the arkers of all fields
            return Stations.objects.filter(station_active=1, map=1)


class SensorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API: return the measures of a sensors according to the ID of the sensor and a date range.
    If the time 'end' is empty, the script search for the latest save measure and return the date/time.
    If the time 'start' is empty, the start time take the value of the end time, minus 3 days.
    Time is UTC zone (Universal Time Coordinated)
    """
    # See serializers.py
    serializer_class = MeasuresSerializer

    def get_queryset(self):
        #get the params
        ids = self.kwargs['idsensor']
        # get the date "from"
        start = self.request.query_params.get('start')
        # get the date "to"
        end = self.request.query_params.get('end')

        # if param end (from) is empty or does not exist
        if end is None or len(end) <= 0:
            # Get the last saved measure date/time of a sensor
            latest_measure = Measures.objects.filter(sensors_id_sensor=ids).order_by('-measure_created').first()
            #save the date
            end = latest_measure.measure_created
        else:
            # get the date from the param end, create an object and save the value to end
            end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

        # if the param start (from) is empty or does not exist
        if start is None or len(start) <= 0:
            # get the date of the latest measure minus 3 days and save it to start
            start = end - timedelta(days=3)
        else:
            # get the value from the param start, create an object and save it to start
            start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')

        # Get all measures from the date range
        sensor_measures = Measures.objects \
            .filter(sensors_id_sensor=ids,
                    measure_created__range=[start,end]) \
            .order_by('measure_created') \
            .select_related('sensors_id_sensor')

        #print(sensor_measures)
        return sensor_measures


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API: return the measures of several sensors according to a type of sensors for a selected field, and a date range.
    (A type is generaly sensors with the same unit (°C, %, kPa))
    If the time 'end' is empty, the today time will be considered
    If the time 'start' is empty, the start time will take the value of the end time, minus 3 days.
    Time is UTC zone (Universal Time Coordinated)
    """
    # See serializers.py
    serializer_class = MeasuresSerializer

    def get_queryset(self):
        # get the params
        idt = self.kwargs['idtype']
        idf = self.kwargs['idfield']
        # get the date "from"
        start = self.request.query_params.get('start')
        # get the date "to"
        end = self.request.query_params.get('end')

        if end is None or len(end) <= 0:
            end = datetime.datetime.now()
        else:
            end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

        if start is None or len(start) <= 0:
            start = end - timedelta(days=3)
        else:
            start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')


        """
        type = SensorTypes.objects.filter(id_sensor_type=idt)
        
        sensors = Sensors.objects.filter(sensor_types_id_sensor_type=idt)\
            .select_related('sensor_types_id_sensor_type')

        print(sensors[0].id_sensor)
        

        for sensor in sensors:
            print(sensor.id_sensor)
        """

        m = Measures.objects.filter(
            sensors_id_sensor__stations_id_station__fields_id_field=idf,
            sensors_id_sensor__sensor_types_id_sensor_type=idt,
            measure_created__range=[start, end]
        ).order_by('measure_created')

        return m



"""
TOKEN
"""
class TestTokenViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MeasuresSerializer
    queryset = Measures.objects.filter(collections_id_collection=50)
    permission_classes = [IsAuthenticated]


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



""" DELETE (I kept the following for record)
def sensor(request,  idsensor):
    if request.method == 'GET':
        # Get the last measure date/time for that sensor
        latest_measure = Measures.objects.filter(sensors_id_sensor=idsensor).order_by('-measure_created').first()

        # Get all measures from 3 days before the last measure
        sensor_measures = Measures.objects\
            .filter(sensors_id_sensor=idsensor, measure_created__range=[latest_measure.measure_created - timedelta(days=3), latest_measure.measure_created])\
            .order_by('measure_created')\
            .select_related('sensors_id_sensor')

        print(request)

        # serialize the task data
        serializer = MeasuresSerializer(sensor_measures, many=True)

        # return a Json response
        return JsonResponse(serializer.data, safe=False)



class SensorsViewSet(viewsets.ReadOnlyModelViewSet):
    
    #API: Get the stations by field
    #See project/urls.py (path("api/map/<int:idfield>/", MarkerViewSet.as_view({'get':'list'}), name="marker_view_set"))
    
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    #queryset = Stations.objects.filter(station_active=1, map=1)
    serializer_class = StationsSerializer

    def get_queryset(self):
        idf = self.kwargs['idfield']
        if idf > 0:
            return Stations.objects.filter(station_active=1, map=1, fields_id_field=idf)
        else:
            return Stations.objects.filter(station_active=1, map=1)

"""

"""
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzI1MTM4NywiaWF0IjoxNjYxOTU1Mzg3LCJqdGkiOiJkN2E3NzRjMDcxZjc0MDA0OWY5M2QwN2Q2MGZmYmUyNiIsInVzZXJfaWQiOjIsInVzZXJuYW1lIjoidG90byJ9.3TDrxmAF_zBP2PtQs0WCsZFqP9nl0k3EaPqeWvk-7-0",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxOTU1Njg3LCJpYXQiOjE2NjE5NTUzODcsImp0aSI6ImIzZjExZTM2Y2M1MDQ1ZDBiMGM3MTY0Y2Y5ODA1M2RiIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ0b3RvIn0.w1CDY0AvE5znLPTsWIbIIPhZXZ8cTvIX6NREwwIZr4w"
}
"""
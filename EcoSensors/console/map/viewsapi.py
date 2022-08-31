#from .models import Stations, Sensors, Measures, Collections
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from datetime import date, timedelta

from .models import Stations, Measures, Sensors
from .serializers import SensorsSerializer,MeasuresSerializer,TypesSerializer
import pickle

""" def sensor can be deleted"""
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

def type(request, idtype):
    if request.method == 'GET':
        # Get the last measure date/time for that sensor
        #latest_measure = Measures.objects.filter(sensor_types_id_sensor_type=idtype).order_by('-measure_created').first()

        # Get all measures from 3 days before the last measure
        sensor_measures = Sensors.objects \
            .filter(sensor_types_id_sensor_type=idtype)

        print(sensor_measures.query)
        # serialize the task data
        serializer = TypesSerializer(sensor_measures, many=True)

        # return a Json response
        return JsonResponse(serializer.data, safe=False)


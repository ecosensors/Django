#from .models import Stations, Sensors, Measures, Collections
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from datetime import date, timedelta

from .models import Measures
from .serializers import SensorsSerializer,MeasuresSerializer
import pickle

""" 
The script bellow is not used any more.
I kept it for record
(can be deleted later)
"""
def sensor(request, idsensor):
    """
    This is the first solution I tried for an API request. I keep it for record.
    The new solution is in viewsets.py (class SensorViewSet(viewsets.ReadOnlyModelViewSet):)
    """
    if request.method == 'GET':
        # Get the last measure date/time for that sensor
        latest_measure = Measures.objects.filter(sensors_id_sensor=idsensor).order_by('-measure_created').first()

        #request.GET.get("idsensor")

        # Get all measures from 3 days before the last measure
        sensor_measures = Measures.objects\
            .filter(sensors_id_sensor=idsensor, measure_created__range=[latest_measure.measure_created - timedelta(days=3), latest_measure.measure_created])\
            .order_by('measure_created')\
            .select_related('sensors_id_sensor')

        # serialize the task data
        serializer = MeasuresSerializer(sensor_measures, many=True)

        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = SensorsSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)



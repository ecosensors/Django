"""Markers API views."""
# Maps with Django (2)
# https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/
#import self
from rest_framework import viewsets
from rest_framework_gis import filters
from datetime import datetime, timedelta
from map.models import Stations, Measures
from map.serializers import StationsSerializer,MeasuresSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API: Retirn les marker des stations
    See project/urlsapi.py (path("api/map/<int:idfield>/", MarkerViewSet.as_view({'get':'list'}), name="marker_view_set"))
    """
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



class SensorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MeasuresSerializer

    def get_queryset(self):
        #get the params
        ids = self.kwargs['idsensor']
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if end is None or len(end) <= 0:
            # Get the last measure date/time for that sensor
            latest_measure = Measures.objects.filter(sensors_id_sensor=ids).order_by('-measure_created').first()
            end = latest_measure.measure_created
        else:
            end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')


        if start is None or len(start) <= 0:
            start = end - timedelta(days=3)
        else:
            start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')

        # Get all measures from 3 days before the last measure
        sensor_measures = Measures.objects \
            .filter(sensors_id_sensor=ids,
                    measure_created__range=[start,end]) \
            .order_by('measure_created') \
            .select_related('sensors_id_sensor')

        #print(sensor_measures)
        return sensor_measures

""" DELETE
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

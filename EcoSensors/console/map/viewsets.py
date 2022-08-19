"""Markers API views."""
# Maps with Django (2)
# https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/
#import self
from rest_framework import viewsets
from rest_framework_gis import filters


from map.models import Stations
from map.serializers import StationsSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Stations.objects.filter(station_active=1, map=1)
    serializer_class = StationsSerializer
    """
    def get_tags(self):
        return Stations.objects.filter(fields_id_field=1)
    """
    def get_queryset(self):
        print("iii",self.kwargs['idfield'])
        #print("ppp:", self.kwargs['idfield'])
        return Stations.objects.filter(fields_id_field=2)


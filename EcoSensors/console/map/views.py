"""
Django © 2022 by Pierre Amey is licensed under CC BY-NC-SA 4.0
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND
"""
import pandas
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from datetime import date, timedelta
from django.views.decorators.cache import cache_page
import json
from django.core import serializers
#from django.core.serializers import serialize

# DjJANGO REST FRAMEWORK
# https://blog.logrocket.com/how-to-build-vue-js-app-django-rest-framework/
## parsing data from the client
from rest_framework.parsers import JSONParser
## To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
## for sending response to the client
from django.http import JsonResponse #, HttpResponse # Already import
## API definition for task

from .serializers import StationsSerializer, MeasuresSerializer
# from django.views.generic.base import TemplateView
from .models import Fields, Stations, Sensors, Measures, Collections


def index(request): #Fields
    """
       TODO, Clean this function as the menu is now include from : {% include "menu.html" with fieldId=id_field %}
    """
    fields_list = Fields.objects.filter(field_active=1) #not used
    return render(request, 'map/home.html', {'fields_list': fields_list, 'id_field': 0,})


def field(request, idfield):
    """
        Get the ID of a field which will be passed in a URL as a param
        That ID is need for leaflet to print the markers of all stations according to the ID of the selected field
    """
    a_field = Fields.objects.filter(id_field=idfield, field_active=1)
    context = {
        'id_field': a_field[0].id_field,
        'field_name': a_field[0].field_name,
        'field_longname': a_field[0].field_longname,
    }

    #s_json = json.dumps(stations_list, indent=4)
    #return HttpResponse(s_json, content_type='application/json')
    return render(request, 'map/field.html', context)


#TODO: Check if we need to delete the cache of a station, when a station have sent a measure. In that case, we could extend the cache duration to 60mn.

@cache_page(120)
def station(request, idfield, idstation):
    """
        To retrieve the information of all sensors according to a station ID.
        To retrieve the values of the sensors of a station
        (The retrieved values will be display in a chart with Chartjs)
        TODO: Add the date form to filter the measure according to date range
    """

    station = Stations.objects.get(id_station=idstation)
    sensors_list = Sensors.objects.filter(stations_id_station=idstation, sensor_active=1)

    measures_by_sensor = []
    for me in sensors_list:
        # save the information of a sensor to a dictionary
        sondes = {
            'id_sensor': me.id_sensor,
            'stations_id_station': me.stations_id_station,
            'sensor_name': me.sensor_name,
            'sensor_longname': me.sensor_longname,
            'sensor_active': me.sensor_active,
            'sensor_created': me.sensor_created,
            'sensor_types_id_sensor_type': me.sensor_types_id_sensor_type,
            'chart_style_id_chart_style': me.chart_style_id_chart_style,
            'chart_pointStyle_id_chart_pointStyle': me.chart_pointstyle_id_chart_pointstyle,
            'chart_borderWidth': me.chart_borderwidth,
            'chart_fill': me.chart_fill,
            'chart_showLine': me.chart_showline,
            'chart_pointRadius': me.chart_pointradius,
            'chart_pointHoverRadius': me.chart_pointhoverradius,
            'chart_backgroundColor_id_chart_backgroundColor': me.chart_backgroundcolor_id_chart_backgroundcolor,
            'chart_borderColor_id_chart_borderColor': me.chart_bordercolor_id_chart_bordercolor,
            'datas': [],
        }

        # get the date of the latest measure of the sensor
        latest_measure = Measures.objects.filter(sensors_id_sensor=me.id_sensor).order_by('-measure_created').first()
        #get the measures from a date range
        for me in Measures.objects.filter(measure_created__range=[latest_measure.measure_created - timedelta(days=3), latest_measure.measure_created],sensors_id_sensor=me.id_sensor).order_by('measure_created'):
            #append the value to sondes
            sondes['datas'].append({
                'measure_created': me.measure_created,
                'value': me.value,
                'sensors_id_sensor': me.sensors_id_sensor,
                'collections_id_collection': me.collections_id_collection,

            })


        measures_by_sensor.append(sondes)

    """ To keep for record
    st = Stations.objects.get(id_station=idstation)
    sensors = st.sensors_set.all()
    s_json = serializers.serialize('json', sensors)
    """

    context ={
        'station': station,
        'sensors': measures_by_sensor,
        'id_field': idfield,
    }


    #s_json = json.dumps(measures_by_sensor, indent=4)
    #return HttpResponse(s_json, content_type='application/json')

    return render(request, 'map/station.html', context)


def sensor(request, idfield, idstation, idsensor):
    """
        To retrieve the information of one sensor according to a sensor ID.
        To retrieve the values of one sensor
        (The retrieved values will be display in a chart with Chartjs)
        TODO: Add the date form to filter the measure according to date range
    """

    sensor = Sensors.objects.get(id_sensor=idsensor)

    # Get the last measure date/time for that sensor
    latest_measure = Measures.objects.filter(sensors_id_sensor=idsensor).order_by('-measure_created').first()
    # Get all measures from 3 days before the last measure
    sensor_measures = Measures.objects.filter(sensors_id_sensor=idsensor, measure_created__range=[latest_measure.measure_created - timedelta(days=3), latest_measure.measure_created]).order_by('measure_created')

    station = Stations.objects.get(id_station=idstation)

    context = {
        'sensor':sensor,
        'station':station,
        'sensor_measures': sensor_measures,
        'id_field' : idfield
    }

    #s_json = json.dumps(station, indent=4)
    #s_json = serializers.serialize('json', s_json)
    #return HttpResponse(s_json, content_type='application/json')
    return render(request, 'map/sensor.html', context)



def debugObject(obj):
    """
    Serialize the values of an object to a json format
    """
    print(obj)
    obj_json = serializers.serialize('json', obj)
    return HttpResponse(obj_json, content_type='application/json')

"""
# The functions bellow are not used any more but I keep them as a record

class IndexView(ListView):
    template_name = 'map/index.html'
    context_object_name = 'fields_list'
    def get_queryset(self):
        return Fields.objects.order_by('-field_created')[:5]


 class FieldsView(DetailView):
    model = Fields
    template_name = 'map/fields.html'


 class StationsView(ListView):
    model = Stations
    context_object_name = 'stations_list'
    template_name = 'map/stations.html'

    def get_queryset(self):
         return Stations.objects.order_by('-station_created')[:10]



#def stations(request, fields_id_field):
    #stations_list = get_object_or_404(Stations, pk=field_id_field)
    stations_list = Stations.objects.filter(fields_id_field=fields_id_field, station_active=1)
    print(stations_list)
    sensors = Sensors.objects.filter(sensor_active=1)

    s = Sensors.objects.filter(Stations__station_longname)
    s = Stations.objects.filter(sensors__sensor_longname)
    s = Sensors.stations_id_station.station_longname(fields_id_field=fields_id_field)

    return render(request, 'map/stations.html', {'stations_list':stations_list, 'sensors':sensors })

class StationView(DetailView):
    model = Stations
    template_name = 'console/station.html'

"""
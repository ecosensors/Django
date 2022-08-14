import pandas
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from datetime import date, timedelta
import json
from django.core import serializers
#from django.core.serializers import serialize



#Django Rest Framework
# https://blog.logrocket.com/how-to-build-vue-js-app-django-rest-framework/
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import JsonResponse #, HttpResponse # Already import
# API definition for task
from .serializers import StationsSerializer



from django.views.generic.base import TemplateView

from .models import Fields, Stations, Sensors, Measures, Collections

class MarkersMapView(TemplateView):
    """Markers map view."""
    template_name = "map/map.html"
    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serializers.serialize("geojson", Stations.objects.all()))
        return context


def index(request): #Fields
    """
        Return the active fields as a menu.
        TODO: Build a google map will all stations and fields
    """
    fields_list = Fields.objects.filter(field_active=1)
    #stations_list = Stations.objects.filter(station_active=1)
    return render(request, 'map/home.html', {'fields_list': fields_list})

def field(request, idfield):
    """
        Get all active fields
        Build a tree with stations and sensors as subtree
    """

    """ Slider section """
    fields_list = Fields.objects.filter(field_active=1)

    stations_list = []
    for st in Stations.objects.filter(fields_id_field=idfield, station_active=1):
        a_stationsonde = {
            'id_station': st.id_station,
            'station_name': st.station_name,
            'station_longname': st.station_longname,
            'fields_id_field': st.fields_id_field.id_field,
            'collection_id': '??',
            'collation_date': '??',
            'sondes': [],
        }

        for se in Sensors.objects.filter(stations_id_station=st.id_station, sensor_active=1):
            a_stationsonde['sondes'].append({
                'id_sensor': se.id_sensor,
                'sensor_name': se.sensor_name,
                'sensor_longname': se.sensor_longname
            })
        stations_list.append(a_stationsonde)

    """ content section """



    context = {
        'stations_list': stations_list,
        'fields_list': fields_list
    }

    #s_json = json.dumps(stations_list, indent=4)
    #return HttpResponse(s_json, content_type='application/json')
    return render(request, 'map/field.html', context)


def station(request, idfield, idstation):
    """
        Get all active fields
        Get a sensor list for matching station
        Build a tree with stations and sensors as subtree
        TODO: Get the measures of all sensor for the selected station
    """

    """ Slider section"""
    fields_list = Fields.objects.filter(field_active=1)

    stations_list = []
    for st in Stations.objects.filter(fields_id_field=idfield, station_active=1):
        a_stationsonde = {
            'id_station': st.id_station,
            'station_name': st.station_name,
            'station_longname': st.station_longname,
            'fields_id_field': st.fields_id_field.id_field,
            'collection_id': '??',
            'collation_date': '??',
            'sondes': [],
        }

        for se in Sensors.objects.filter(stations_id_station=st.id_station, sensor_active=1):
            a_stationsonde['sondes'].append({
                'id_sensor': se.id_sensor,
                'sensor_name': se.sensor_name,
                'sensor_longname': se.sensor_longname
            })

        stations_list.append(a_stationsonde)

    """ Content section """
    station = Stations.objects.get(id_station=idstation)
    sensors_list = Sensors.objects.filter(stations_id_station=idstation, sensor_active=1)

    measures_by_sensor = []
    for me in sensors_list:
        print(me.sensor_name, me.id_sensor)
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
        latest_measure = Measures.objects.filter(sensors_id_sensor=me.id_sensor).order_by('-measure_created').first()

        for me in Measures.objects.filter(measure_created__range=[latest_measure.measure_created - timedelta(days=3), latest_measure.measure_created],sensors_id_sensor=me.id_sensor).order_by('measure_created'):

            sondes['datas'].append({
                'measure_created': me.measure_created,
                'value': me.value,
                'sensors_id_sensor': me.sensors_id_sensor,
                'collections_id_collection': me.collections_id_collection,
            })


        measures_by_sensor.append(sondes)

    """ Test panda and Matplotlib """
    """
    mesures = Measures.objects.filter(measure_created__range=["2022-05-2 10:00:00", "2022-05-2 20:22:00"],
                                          sensors_id_sensor=72).order_by('-measure_created')
    sales_df = pandas.DataFrame(mesures.values())
    print('panda:', sales_df)
    """



    """ A agrder
    st = Stations.objects.get(id_station=idstation)
    sensors = st.sensors_set.all()
    s_json = serializers.serialize('json', sensors)

    m = Measures.objects.filter(measure_created__range=["2022-07-2 20:00:00", "2022-07-2 20:22:00"], collections_id_collection=263971)
    measures = m.  .all()
    """

    context ={
        'station': station,
        'sensors': measures_by_sensor,
        'fields_list': fields_list,
        'stations_list': stations_list
    }


    #s_json = json.dumps(measures_by_sensor, indent=4)
    #return HttpResponse(s_json, content_type='application/json')

    return render(request, 'map/station.html', context)

def sensor(request, idfield, idstation, idsensor):
    """
        Get all active fields
        Get a sensor list for matching station
        Build a tree with stations and sensors as subtree
        Get information for one selected sensor according to a date range (TO DO)
        Get information for one selected station
    """

    """ Slider section """
    fields_list = Fields.objects.filter(field_active=1)

    stations_list = []
    for st in Stations.objects.filter(fields_id_field=idfield, station_active=1):
        a_stationsonde = {
            'id_station': st.id_station,
            'station_name': st.station_name,
            'station_longname': st.station_longname,
            'fields_id_field': st.fields_id_field.id_field,
            'collection_id': '??',
            'collation_date': '??',
            'sondes': [],
        }

        for se in Sensors.objects.filter(stations_id_station=st.id_station, sensor_active=1):
            a_stationsonde['sondes'].append({
                'id_sensor': se.id_sensor,
                'sensor_name': se.sensor_name,
                'sensor_longname': se.sensor_longname
            })

        stations_list.append(a_stationsonde)

    """ Content section """
    sensor = Sensors.objects.get(id_sensor=idsensor)

    # Get the last measure date/time for that sensor
    latest_measure = Measures.objects.filter(sensors_id_sensor=idsensor).order_by('-measure_created').first()
    # Get all measures from 3 days before the last measure
    sensor_measures = Measures.objects.filter(sensors_id_sensor=idsensor, measure_created__range=[latest_measure.measure_created - timedelta(days=3), latest_measure.measure_created]).order_by('measure_created')

    #DEL Measures.objects.filter(measure_created__range=[latest_measure.measure_created - timedelta(days=1), latest_measure.measure_created],sensors_id_sensor=me.id_sensor).order_by('measure_created'):


    station = Stations.objects.get(id_station=idstation)

    context = {
        'sensor':sensor,
        'station':station,
        'sensor_measures': sensor_measures,
        'fields_list': fields_list,
        'stations_list': stations_list
    }

    #s_json = json.dumps(station, indent=4)
    #s_json = serializers.serialize('json', s_json)
    #return HttpResponse(s_json, content_type='application/json')
    return render(request, 'map/sensor.html', context)



# DRF

def api(request, idfield):
    '''
    Exercise with Django Rest Framework (GET/POST)
    https://blog.logrocket.com/how-to-build-vue-js-app-django-rest-framework/#setting-up-vuejs-client-app
    '''
    if(request.method == 'GET'):
        # get all the tasks
        stations = Stations.objects.filter(fields_id_field=idfield, station_active=1)
        # serialize the task data
        serializer = StationsSerializer(stations, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = StationsSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)






def debugObject(obj):
    print(obj)
    obj_json = serializers.serialize('json', obj)
    return HttpResponse(obj_json, content_type='application/json')

def aside(request):
    """Return the active fields."""
    fields = Fields.objects.filter(field_active=1)
    fields.stations_set.all()
    #st = {}
    #for e in Fields.objects.filter(field_active=1):
    #    print(e.field_name)
    #    st[e.id_field] = Stations.objects.filter(station_active=1, id_field=e.id_field)

    return render(request, 'map/slider.html')


#class IndexView(ListView):
#    template_name = 'map/index.html'
#    context_object_name = 'fields_list'
#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Fields.objects.order_by('-field_created')[:5]


# class FieldsView(DetailView):
#    model = Fields
#    template_name = 'map/fields.html'


# class StationsView(ListView):
#    model = Stations
#    context_object_name = 'stations_list'
#    template_name = 'map/stations.html'
#
#    def get_queryset(self):
#        """Return the last five published station."""
#         return Stations.objects.order_by('-station_created')[:10]



#def stations(request, fields_id_field):
    #stations_list = get_object_or_404(Stations, pk=field_id_field)
#    stations_list = Stations.objects.filter(fields_id_field=fields_id_field, station_active=1)
#    print(stations_list)
#    sensors = Sensors.objects.filter(sensor_active=1)

    #s = Sensors.objects.filter(Stations__station_longname)
    #s = Stations.objects.filter(sensors__sensor_longname)
    #s = Sensors.stations_id_station.station_longname(fields_id_field=fields_id_field)

 #   return render(request, 'map/stations.html', {'stations_list':stations_list, 'sensors':sensors })

#class StationView(DetailView):
#    model = Stations
#    template_name = 'console/station.html'
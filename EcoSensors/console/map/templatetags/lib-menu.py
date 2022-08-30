from django import template
from django.views.decorators.cache import cache_page
from map.models import Fields, Stations, Sensors, Measures, Collections
register = template.Library()


@cache_page(1800)
@register.simple_tag
def menuFields():
    """
    Display all active fields
    """
    fields_list = Fields.objects.filter(field_active=1)  # Get all active fields
    return fields_list


@cache_page(1800)
@register.simple_tag
def menuStations(fieldid):
    """
    Display all active stations according to a selected field
    As a subtree, display all sensors for a station
    """
    stations_list = []  # Initiate a list to store the stations according to the filed id
    # Query the active station according to a selected field
    for st in Stations.objects.filter(fields_id_field=fieldid, station_active=1):
        a_stationsonde = {
            'id_station': st.id_station,
            'station_name': st.station_name,
            'station_longname': st.station_longname,
            'fields_id_field': st.fields_id_field.id_field,
            'collection_id': '??',
            'collation_date': '??',
            'sondes': [],
        }
        # Query the active sensor according to a station id
        for se in Sensors.objects.filter(stations_id_station=st.id_station, sensor_active=1):
            a_stationsonde['sondes'].append({
                'id_sensor': se.id_sensor,
                'sensor_name': se.sensor_name,
                'sensor_longname': se.sensor_longname
            })
        # Append a station information to the station list
        stations_list.append(a_stationsonde)

    return stations_list
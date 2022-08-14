from django.contrib import admin
from .models import Fields, Stations, Sensors

class FieldsAdmin(admin.ModelAdmin):
    list_display = ("id_field", "field_active", "field_name", "field_longname", "field_lat", "field_lng", "field_alt", "cp", "city", "states_id_state", "field_created")
    list_editable = ("field_name", "field_longname", "field_lat", "field_lng", "field_alt", "cp", "city", "states_id_state", "field_active")

admin.site.register(Fields, FieldsAdmin)

class StationsAdmin(admin.ModelAdmin):
    list_display = ("id_station", "station_active", "station_name", "station_longname", "fields_id_field", "station_lat", "station_lng", "station_created", "map")
    list_editable = ("station_name", "station_longname", "station_lat", "station_lng", "station_active", "map")

admin.site.register(Stations, StationsAdmin)

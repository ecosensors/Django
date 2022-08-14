# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point


class ChartBackgroundcolor(models.Model):
    id_chart_backgroundcolor = models.AutoField(db_column='id_chart_backgroundColor', primary_key=True)  # Field name made lowercase.
    colors_id_colors = models.ForeignKey('Colors', models.DO_NOTHING, db_column='colors_id_colors')

    class Meta:
        managed = False
        db_table = 'chart_backgroundColor'


class ChartBordercolor(models.Model):
    id_chart_bordercolor = models.AutoField(db_column='id_chart_borderColor', primary_key=True)  # Field name made lowercase.
    colors_id_colors = models.ForeignKey('Colors', models.DO_NOTHING, db_column='colors_id_colors')

    class Meta:
        managed = False
        db_table = 'chart_borderColor'


class ChartPointstyle(models.Model):
    id_chart_pointstyle = models.AutoField(db_column='id_chart_pointStyle', primary_key=True)  # Field name made lowercase.
    chart_pointstyle_name = models.CharField(db_column='chart_pointStyle_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    chart_pointstyle_value = models.CharField(db_column='chart_pointStyle_value', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chart_pointStyle'


class ChartStyle(models.Model):
    id_chart_style = models.AutoField(primary_key=True)
    chart_style_name = models.CharField(max_length=45, blank=True, null=True)
    chart_style_value = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chart_style'


class Collections(models.Model):
    id_collection = models.AutoField(primary_key=True)
    gateways_id_gateway = models.IntegerField()
    hardware_serial = models.CharField(max_length=30)
    ttn_port = models.IntegerField()
    ttn_counter = models.IntegerField()
    ttn_payload_raw = models.CharField(max_length=45)
    ttn_m_time = models.DateTimeField()
    ttn_m_freq = models.DecimalField(max_digits=4, decimal_places=1)
    g_rssi = models.IntegerField()
    g_channel = models.IntegerField()
    g_snr = models.IntegerField()
    g_sf = models.IntegerField(blank=True, null=True)
    g_bandwith = models.IntegerField(blank=True, null=True)
    ttn_m_modulation = models.CharField(max_length=25)
    ttn_m_data_rate = models.CharField(max_length=25, blank=True, null=True)
    ttn_m_coding_rate = models.CharField(max_length=10)
    collection_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'collections'


class Colors(models.Model):
    id_colors = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=45, blank=True, null=True)
    color_value = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colors'


class Cordova(models.Model):
    id_version = models.AutoField(primary_key=True)
    isanupdate = models.IntegerField(db_column='isAnUpdate')  # Field name made lowercase.
    version = models.CharField(max_length=10)
    beta = models.IntegerField()
    description = models.TextField()
    active = models.IntegerField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cordova'


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=45, blank=True, null=True)
    country_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Fields(models.Model):
    id_field = models.AutoField(primary_key=True)
    countries_country = models.ForeignKey(Countries, models.DO_NOTHING)
    states_id_state = models.ForeignKey('States', models.DO_NOTHING, db_column='states_id_state')
    field_name = models.CharField(max_length=20)
    field_longname = models.CharField(max_length=45, blank=True, null=True)
    field_lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    field_lng = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    field_alt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    cp = models.CharField(max_length=45, blank=True, null=True)
    field_created = models.DateTimeField()
    field_active = models.BooleanField()

    #def __str__(self):
    #    return '[%s] %s' % (self.id_field, self.field_longname)

    class Meta:
        managed = False
        db_table = 'fields'


class FieldsHasUsers(models.Model):
    fields_id_field = models.IntegerField()
    users_id_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fields_has_users'


class Gateways(models.Model):
    id_gateway = models.AutoField(primary_key=True)
    gtw_id = models.CharField(max_length=45, blank=True, null=True)
    gtw_eui = models.CharField(max_length=45, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    channel = models.IntegerField(blank=True, null=True)
    rssi = models.IntegerField(blank=True, null=True)
    snr = models.IntegerField(blank=True, null=True)
    rf_chain = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    altitude = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gateways'


class Historicals(models.Model):
    id_historical = models.AutoField(primary_key=True)
    stations_id_station = models.IntegerField(blank=True, null=True)
    historicals_title = models.CharField(max_length=100)
    historicals_description = models.TextField()
    historicals_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'historicals'


class Measures(models.Model):
    id_measure = models.AutoField(primary_key=True)
    sensors_id_sensor = models.ForeignKey('Sensors', models.DO_NOTHING, db_column='sensors_id_sensor')
    collections_id_collection = models.ForeignKey(Collections, models.DO_NOTHING, db_column='collections_id_collection')
    value = models.DecimalField(max_digits=11, decimal_places=4)
    measure_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'measures'


class Roles(models.Model):
    id_role = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'roles'


class SensorFamilies(models.Model):
    id_sensor_family = models.AutoField(primary_key=True)
    sensor_family_name = models.CharField(max_length=45)
    sensor_family_longname = models.CharField(max_length=45, blank=True, null=True)
    sensor_family_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensor_families'


class SensorNames(models.Model):
    id_sensor_name = models.AutoField(primary_key=True)
    sensor_name = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sensor_names'


class SensorTypes(models.Model):
    id_sensor_type = models.AutoField(primary_key=True)
    sensor_families_id_sensor_family = models.ForeignKey(SensorFamilies, models.DO_NOTHING, db_column='sensor_families_id_sensor_family')
    sensor_type_name = models.CharField(max_length=20)
    sensor_type_longname = models.CharField(max_length=45, blank=True, null=True)
    sensor_type_description = models.CharField(max_length=255, blank=True, null=True)
    sensor_type_longdescription = models.TextField(blank=True, null=True)
    measure_unit = models.CharField(max_length=5)
    sensor_type_created = models.DateTimeField()
    sensor_type_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensor_types'


class Sensors(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    stations_id_station = models.ForeignKey('Stations', models.DO_NOTHING, db_column='stations_id_station')
    sensor_types_id_sensor_type = models.ForeignKey(SensorTypes, models.DO_NOTHING, db_column='sensor_types_id_sensor_type')
    sensor_name = models.CharField(max_length=20)
    sensor_longname = models.CharField(max_length=45, blank=True, null=True)
    sensor_description = models.TextField(blank=True, null=True)
    sensor_active = models.IntegerField(blank=True, null=True)
    sensor_created = models.DateTimeField()
    chart_style_id_chart_style = models.ForeignKey(ChartStyle, models.DO_NOTHING, db_column='chart_style_id_chart_style')
    chart_pointstyle_id_chart_pointstyle = models.ForeignKey(ChartPointstyle, models.DO_NOTHING, db_column='chart_pointStyle_id_chart_pointStyle')  # Field name made lowercase.
    chart_borderwidth = models.IntegerField(db_column='chart_borderWidth', blank=True, null=True)  # Field name made lowercase.
    chart_fill = models.IntegerField(blank=True, null=True)
    chart_showline = models.IntegerField(db_column='chart_showLine', blank=True, null=True)  # Field name made lowercase.
    chart_pointradius = models.IntegerField(db_column='chart_pointRadius', blank=True, null=True)  # Field name made lowercase.
    chart_pointhoverradius = models.IntegerField(db_column='chart_pointHoverRadius', blank=True, null=True)  # Field name made lowercase.
    chart_backgroundcolor_id_chart_backgroundcolor = models.ForeignKey(ChartBackgroundcolor, models.DO_NOTHING, db_column='chart_backgroundColor_id_chart_backgroundColor')  # Field name made lowercase.
    chart_bordercolor_id_chart_bordercolor = models.ForeignKey(ChartBordercolor, models.DO_NOTHING, db_column='chart_borderColor_id_chart_borderColor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sensors'


class States(models.Model):
    id_state = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=45, blank=True, null=True)
    state_code = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.state_name)

    class Meta:
        managed = False
        db_table = 'states'


class Stations(models.Model):
    id_station = models.AutoField(primary_key=True)
    fields_id_field = models.ForeignKey(Fields, models.DO_NOTHING, db_column='fields_id_field')
    stations_types_id_stations_type = models.IntegerField()
    station_name = models.CharField(max_length=20)
    station_longname = models.CharField(max_length=45, blank=True, null=True)
    station_active = models.BooleanField()
    station_archive = models.BooleanField()
    location = PointField(blank=True, null=True, srid=4326)
    station_lat = models.FloatField(blank=True, null=True)
    station_lng = models.FloatField(blank=True, null=True)
    station_alt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    installed = models.DateTimeField()
    station_description = models.TextField(blank=True, null=True)
    ttn_app_id = models.CharField(max_length=20)
    ttn_dev_id = models.CharField(max_length=20)
    ttn_hardware_serial = models.CharField(max_length=20)
    station_created = models.DateTimeField()
    station_order = models.IntegerField()
    map = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'stations'

    def save(self, *args, **kwargs):
        self.location = Point(float(self.station_lng), float(self.station_lat))
        super(Stations, self).save(*args, **kwargs)



class StationsTypes(models.Model):
    id_stations_type = models.AutoField(primary_key=True)
    stations_type_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'stations_types'


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    roles_id_role = models.IntegerField()
    user_firstname = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=100)
    user_email = models.CharField(max_length=50)
    user_mdp = models.CharField(max_length=255)
    user_active = models.IntegerField()
    user_create = models.DateTimeField()
    user_lastlogin = models.DateTimeField(blank=True, null=True)
    user_failedlogin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

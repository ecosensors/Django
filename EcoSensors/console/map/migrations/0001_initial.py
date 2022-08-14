# Generated by Django 4.0.6 on 2022-07-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChartBackgroundcolor',
            fields=[
                ('id_chart_backgroundcolor', models.AutoField(db_column='id_chart_backgroundColor', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'chart_backgroundColor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChartBordercolor',
            fields=[
                ('id_chart_bordercolor', models.AutoField(db_column='id_chart_borderColor', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'chart_borderColor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChartPointstyle',
            fields=[
                ('id_chart_pointstyle', models.AutoField(db_column='id_chart_pointStyle', primary_key=True, serialize=False)),
                ('chart_pointstyle_name', models.CharField(blank=True, db_column='chart_pointStyle_name', max_length=45, null=True)),
                ('chart_pointstyle_value', models.CharField(blank=True, db_column='chart_pointStyle_value', max_length=45, null=True)),
            ],
            options={
                'db_table': 'chart_pointStyle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChartStyle',
            fields=[
                ('id_chart_style', models.AutoField(primary_key=True, serialize=False)),
                ('chart_style_name', models.CharField(blank=True, max_length=45, null=True)),
                ('chart_style_value', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'chart_style',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id_collection', models.AutoField(primary_key=True, serialize=False)),
                ('gateways_id_gateway', models.IntegerField()),
                ('hardware_serial', models.CharField(max_length=30)),
                ('ttn_port', models.IntegerField()),
                ('ttn_counter', models.IntegerField()),
                ('ttn_payload_raw', models.CharField(max_length=45)),
                ('ttn_m_time', models.DateTimeField()),
                ('ttn_m_freq', models.DecimalField(decimal_places=1, max_digits=4)),
                ('g_rssi', models.IntegerField()),
                ('g_channel', models.IntegerField()),
                ('g_snr', models.IntegerField()),
                ('g_sf', models.IntegerField(blank=True, null=True)),
                ('g_bandwith', models.IntegerField(blank=True, null=True)),
                ('ttn_m_modulation', models.CharField(max_length=25)),
                ('ttn_m_data_rate', models.CharField(blank=True, max_length=25, null=True)),
                ('ttn_m_coding_rate', models.CharField(max_length=10)),
                ('collection_created', models.DateTimeField()),
            ],
            options={
                'db_table': 'collections',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id_colors', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(blank=True, max_length=45, null=True)),
                ('color_value', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'colors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cordova',
            fields=[
                ('id_version', models.AutoField(primary_key=True, serialize=False)),
                ('isanupdate', models.IntegerField(db_column='isAnUpdate')),
                ('version', models.CharField(max_length=10)),
                ('beta', models.IntegerField()),
                ('description', models.TextField()),
                ('active', models.IntegerField()),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'cordova',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=45, null=True)),
                ('country_code', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id_field', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(max_length=20)),
                ('field_longname', models.CharField(blank=True, max_length=45, null=True)),
                ('field_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('field_lng', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('field_alt', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('threshold', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('cp', models.CharField(blank=True, max_length=45, null=True)),
                ('field_created', models.DateTimeField()),
                ('field_active', models.IntegerField()),
            ],
            options={
                'db_table': 'fields',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FieldsHasUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields_id_field', models.IntegerField()),
                ('users_id_user', models.IntegerField()),
            ],
            options={
                'db_table': 'fields_has_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gateways',
            fields=[
                ('id_gateway', models.AutoField(primary_key=True, serialize=False)),
                ('gtw_id', models.CharField(blank=True, max_length=45, null=True)),
                ('gtw_eui', models.CharField(blank=True, max_length=45, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('channel', models.IntegerField(blank=True, null=True)),
                ('rssi', models.IntegerField(blank=True, null=True)),
                ('snr', models.IntegerField(blank=True, null=True)),
                ('rf_chain', models.IntegerField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('altitude', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'gateways',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historicals',
            fields=[
                ('id_historical', models.AutoField(primary_key=True, serialize=False)),
                ('stations_id_station', models.IntegerField(blank=True, null=True)),
                ('historicals_title', models.CharField(max_length=100)),
                ('historicals_description', models.TextField()),
                ('historicals_date', models.DateField()),
            ],
            options={
                'db_table': 'historicals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Measures',
            fields=[
                ('id_measure', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=4, max_digits=11)),
                ('measure_created', models.DateTimeField()),
            ],
            options={
                'db_table': 'measures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_role', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorFamilies',
            fields=[
                ('id_sensor_family', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_family_name', models.CharField(max_length=45)),
                ('sensor_family_longname', models.CharField(blank=True, max_length=45, null=True)),
                ('sensor_family_order', models.IntegerField()),
            ],
            options={
                'db_table': 'sensor_families',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorNames',
            fields=[
                ('id_sensor_name', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_name', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'sensor_names',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id_sensor', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_name', models.CharField(max_length=20)),
                ('sensor_longname', models.CharField(blank=True, max_length=45, null=True)),
                ('sensor_description', models.TextField(blank=True, null=True)),
                ('sensor_active', models.IntegerField(blank=True, null=True)),
                ('sensor_created', models.DateTimeField()),
                ('chart_borderwidth', models.IntegerField(blank=True, db_column='chart_borderWidth', null=True)),
                ('chart_fill', models.IntegerField(blank=True, null=True)),
                ('chart_showline', models.IntegerField(blank=True, db_column='chart_showLine', null=True)),
                ('chart_pointradius', models.IntegerField(blank=True, db_column='chart_pointRadius', null=True)),
                ('chart_pointhoverradius', models.IntegerField(blank=True, db_column='chart_pointHoverRadius', null=True)),
            ],
            options={
                'db_table': 'sensors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorTypes',
            fields=[
                ('id_sensor_type', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_type_name', models.CharField(max_length=20)),
                ('sensor_type_longname', models.CharField(blank=True, max_length=45, null=True)),
                ('sensor_type_description', models.CharField(blank=True, max_length=255, null=True)),
                ('sensor_type_longdescription', models.TextField(blank=True, null=True)),
                ('measure_unit', models.CharField(max_length=5)),
                ('sensor_type_created', models.DateTimeField()),
                ('sensor_type_order', models.IntegerField()),
            ],
            options={
                'db_table': 'sensor_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id_state', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, max_length=45, null=True)),
                ('state_code', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'states',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id_station', models.AutoField(primary_key=True, serialize=False)),
                ('stations_types_id_stations_type', models.IntegerField()),
                ('station_name', models.CharField(max_length=20)),
                ('station_longname', models.CharField(blank=True, max_length=45, null=True)),
                ('station_active', models.IntegerField()),
                ('station_archive', models.IntegerField()),
                ('station_lat', models.FloatField(blank=True, null=True)),
                ('station_lng', models.FloatField(blank=True, null=True)),
                ('station_alt', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('installed', models.DateTimeField()),
                ('station_description', models.TextField(blank=True, null=True)),
                ('ttn_app_id', models.CharField(max_length=20)),
                ('ttn_dev_id', models.CharField(max_length=20)),
                ('ttn_hardware_serial', models.CharField(max_length=20)),
                ('station_created', models.DateTimeField()),
                ('station_order', models.IntegerField()),
                ('map', models.IntegerField()),
            ],
            options={
                'db_table': 'stations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StationsTypes',
            fields=[
                ('id_stations_type', models.AutoField(primary_key=True, serialize=False)),
                ('stations_type_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'stations_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('roles_id_role', models.IntegerField()),
                ('user_firstname', models.CharField(max_length=100)),
                ('user_lastname', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=50)),
                ('user_mdp', models.CharField(max_length=255)),
                ('user_active', models.IntegerField()),
                ('user_create', models.DateTimeField()),
                ('user_lastlogin', models.DateTimeField(blank=True, null=True)),
                ('user_failedlogin', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]

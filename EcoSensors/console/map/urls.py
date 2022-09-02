"""
Django © 2022 by Pierre Amey is licensed under CC BY-NC-SA 4.0
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND
"""
from django.urls import path
from . import views

app_name="map"
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('field/<int:idfield>', views.field, name='field'),
    path('field/<int:idfield>/station/<int:idstation>', views.station, name='station'),
    path('field/<int:idfield>/station/<int:idstation>/sensor/<int:idsensor>', views.sensor, name='sensor'),

]
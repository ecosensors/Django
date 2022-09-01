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
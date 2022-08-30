from django.urls import path
from map.viewsets import MarkerViewSet
from . import views
# from .views import MarkersMapView # (Maps with Django (1))

app_name="map"
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('field/<int:idfield>', views.field, name='field'),
    path('field/<int:idfield>/station/<int:idstation>', views.station, name='station'),
    path('field/<int:idfield>/station/<int:idstation>/sensor/<int:idsensor>', views.sensor, name='sensor'),
    #path('<int:idstation>/sensors', views.sensors, name='sensors'),
    #path('<int:pk>/station/', views.StationView.as_view(), name='station'),
]
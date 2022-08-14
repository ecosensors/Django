from django.urls import path
from . import views
from .views import MarkersMapView

app_name="map"
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path("mapy/", MarkersMapView.as_view()),
    path('<int:idfield>/field', views.field, name='field'),
    path('<int:idfield>/<int:idstation>/station', views.station, name='station'),
    path('<int:idfield>/<int:idstation>/<int:idsensor>/sensor', views.sensor, name='sensor'),
    path('<int:idfield>/', views.api, name='api'),

    #path('<int:idstation>/sensors', views.sensors, name='sensors'),
    #path('<int:pk>/station/', views.StationView.as_view(), name='station'),
]
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
    ## Path pour récupérer les Token (attention, il faudra ajouter des import: import TokenRefrehView et MyObtainTokenPairView
    ## from rest_framework_simplejwt.views import TokenRefreshView
    #path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
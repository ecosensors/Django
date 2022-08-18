"""Markers API URL Configuration."""
# Maps with Django (2)
# https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/
from rest_framework import routers
from map.viewsets import MarkerViewSet

router = routers.DefaultRouter()
router.register(r"map", MarkerViewSet)
#router.register(r"^map/{idf}/$", MarkerViewSet)

urlpatterns = router.urls


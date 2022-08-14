"""Markers API URL Configuration."""

from rest_framework import routers

from map.viewsets import MarkerViewSet

router = routers.DefaultRouter()
router.register(r"map", MarkerViewSet)

urlpatterns = router.urls


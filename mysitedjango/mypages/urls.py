from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from mypages.views import (
    favgamesViewSet,
    ModslistViewSet,
    GraphsViewSet,
    ModelTimeRecordscsvViewSet,
)

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register(r"favgames", favgamesViewSet)
router.register(r"modslists", ModslistViewSet)
router.register(r"graphs", GraphsViewSet)
router.register(r"BaseTimeRecords", ModelTimeRecordscsvViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

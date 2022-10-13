from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'favegames', views.FavegamesViewSet)
router.register(r'modslist', views.ModslistViewSet)

# app_name = "mypages"
urlpatterns = [
    path("", include(router.urls)),
]
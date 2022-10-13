from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponse
from .models import favegames, modslist
from .forms import favegamesform, modslistform
from .serializers import FavegamesSerializer, ModslistSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, renderers, viewsets

class FavegamesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = favegames.objects.all()
    serializer_class = FavegamesSerializer

class ModslistViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = modslist.objects.all()
    serializer_class = ModslistSerializer
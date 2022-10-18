from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponse
from mypages.models import favgames, modslists, graphs
from mypages.forms import favgamesform, modslistform, graphsform
from mypages.serializers import FavgamesSerializer, ModslistSerializer, GraphsSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import (
    generics,
    permissions,
    renderers,
    viewsets,
    exceptions,
)
import rest_framework.parsers
import rest_framework.renderers
import rest_framework_json_api.parsers
import rest_framework_json_api.metadata
import rest_framework_json_api.renderers
from rest_framework_json_api.utils import format_drf_errors
from rest_framework_json_api.views import ModelViewSet

HTTP_422_UNPROCESSABLE_ENTITY = 422


class JsonApiViewSet(ModelViewSet):
    """
    This is an example on how to configure DRF-jsonapi from
    within a class. It allows using DRF-jsonapi alongside
    vanilla DRF API views.
    """

    parser_classes = [
        rest_framework_json_api.parsers.JSONParser,
        rest_framework.parsers.FormParser,
        rest_framework.parsers.MultiPartParser,
    ]
    renderer_classes = [
        rest_framework_json_api.renderers.JSONRenderer,
        rest_framework.renderers.BrowsableAPIRenderer,
    ]
    metadata_class = rest_framework_json_api.metadata.JSONAPIMetadata

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.ValidationError):
            # some require that validation errors return 422 status
            # for example ember-data (isInvalid method on adapter)
            exc.status_code = HTTP_422_UNPROCESSABLE_ENTITY
        # exception handler can't be set on class so you have to
        # override the error response in this method
        response = super(JsonApiViewSet, self).handle_exception(exc)
        context = self.get_exception_handler_context()
        return format_drf_errors(response, context, exc)


class favgamesViewSet(JsonApiViewSet):
    
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = favgames.objects.all()
    serializer_class = FavgamesSerializer


class ModslistViewSet(JsonApiViewSet):
    
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = modslists.objects.all()
    serializer_class = ModslistSerializer
    
class GraphsViewSet(JsonApiViewSet):
    
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = graphs.objects.all()
    serializer_class = GraphsSerializer

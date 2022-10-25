from rest_framework_json_api import serializers
from mypages.models import favgames, modslists, graphs, modeltimerecordscsv


class FavgamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = favgames
        fields = ["id", "gamename", "startyear", "url"]


class ModslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = modslists
        fields = [
            "id",
            "modname",
            "releaseyear",
            "game",
            "link",
            "image",
            "url",
        ]


class GraphsSerializer(serializers.ModelSerializer):
    class Meta:
        model = graphs
        fields = ["id", "graphname", "graphlink", "url"]


class ModelTimerecordscsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeltimerecordscsv
        fields = [
            "id",
            "date",
            "user",
            "minutes",
            "ticket",
            "code",
            "billable",
            "url",
        ]

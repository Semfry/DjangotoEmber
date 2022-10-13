from rest_framework_json_api import serializers
from mypages.models import favgames, modslists


class favgamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = favgames
        fields = ["id", "gamename", "startyear", "url"]

    # def create(self, validated_data):
    #     """
    #     Create and return a new `favgames` instance, given the validated data.
    #     """
    #     return favgames.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `favgames` instance, given the validated data.
    #     """
    #     instance.gamename = validated_data.get('gamename', instance.gamename)
    #     instance.startyear = validated_data.get('startyear', instance.startyear)
    #     instance.save()
    #     return instance


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

    # def create(self, validated_data):
    #     """
    #     Create and return a new `modslists` instance, given the validated data.
    #     """
    #     return modslists.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `modslists` instance, given the validated data.
    #     """
    #     instance.modname= validated_data.get('modname', instance.modname)
    #     instance.releaseyear = validated_data.get('releaseyear', instance.releaseyear)
    #     instance.game = validated_data.get('game', instance.game)
    #     instance.link = validated_data.get('link', instance.link)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.save()
    #     return instance

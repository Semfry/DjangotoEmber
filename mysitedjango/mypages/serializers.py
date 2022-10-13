from rest_framework_json_api import serializers
from .models import favegames, modslist

class FavegamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = favegames
        fields = ["url", "id", "gamename", "startyear"]

    def create(self, validated_data):
        """
        Create and return a new `favegames` instance, given the validated data.
        """
        return favegames.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `favegames` instance, given the validated data.
        """
        instance.gamename = validated_data.get('gamename', instance.gamename)
        instance.startyear = validated_data.get('startyear', instance.startyear)
        instance.save()
        return instance
    
class ModslistSerializer(serializers.ModelSerializer):

    class Meta:
        model = modslist
        fields = ["url", "id", "modname", "releaseyear", "game", "link", "image"]

    def create(self, validated_data):
        """
        Create and return a new `modslist` instance, given the validated data.
        """
        return modslist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `modslist` instance, given the validated data.
        """
        instance.modname= validated_data.get('modname', instance.modname)
        instance.releaseyear = validated_data.get('releaseyear', instance.releaseyear)
        instance.game = validated_data.get('game', instance.game)
        instance.link = validated_data.get('link', instance.link)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
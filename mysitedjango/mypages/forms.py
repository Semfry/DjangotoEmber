from django import forms
from django.forms import ModelForm, TextInput, DateInput
from django.core.exceptions import ValidationError
from mypages.models import favgames, modslists, graphs, modeltimerecordscsv


class favgamesform(ModelForm):
    class Meta:
        model = favgames
        fields = ["gamename", "startyear"]


class modslistform(ModelForm):
    class Meta:
        model = modslists
        fields = ["modname", "releaseyear", "game", "link", "image"]


class graphsform(ModelForm):
    class Meta:
        model = graphs
        fields = ["graphname", "graphlink"]


class modeltimerecordscsvform(ModelForm):
    class Meta:
        model = modeltimerecordscsv
        fields = [
            "date",
            "user",
            "minutes",
            "ticket",
            "code",
            "billable",
        ]

from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class favgames(models.Model):
    gamename = models.CharField(
        "name of game/series", max_length=100, blank=True, default=""
    )
    startyear = models.DateField(
        "release year/start of series (format DD/MM/YY)"
    )

    class Meta:
        ordering = ("id",)


class modslists(models.Model):
    modname = models.CharField(
        "name of mod", max_length=100, blank=True, default=""
    )
    releaseyear = models.DateField(
        "release year/start of series (format DD/MM/YY)"
    )
    game = models.CharField(
        "name of game", max_length=100, blank=True, default=""
    )
    link = models.URLField(max_length=200, default="admin/mypages/mods/")
    image = models.ImageField(upload_to="static/images")

    class Meta:
        ordering = ("id",)


class graphs(models.Model):
    graphname = models.CharField(
        "name of chart", max_length=100, blank=True, default=""
    )
    graphlink = models.ImageField(upload_to="static/images/graphs")

    class Meta:
        ordering = ("id",)


class modeltimerecordscsv(models.Model):
    date = models.DateField(blank=True, null=True)
    user = models.CharField(max_length=200)
    minutes = models.FloatField()
    ticket = models.IntegerField()
    code = models.CharField(max_length=200)
    billable = models.CharField(max_length=200)

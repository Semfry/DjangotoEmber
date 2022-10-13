from django.db import models
from django.core.exceptions import ValidationError
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# Create your models here.

class favegames(models.Model):
    gamename = models.CharField("name of game/series", max_length=100, blank=True, default="")
    startyear = models.DateField("release year/start of series (format DD/MM/YY)")
    
    class Meta:
	    ordering = ('id',)
    
class modslist(models.Model):
    modname = models.CharField("name of mod", max_length=100, blank=True, default="")
    releaseyear = models.DateField("release year/start of series (format DD/MM/YY)")
    game = models.CharField("name of game", max_length=100, blank=True, default="")
    link = models.URLField(max_length=200, default="admin/mypages/mods/")
    image = models.ImageField(upload_to="static/images")
    
    class Meta:
	    ordering = ('id',)
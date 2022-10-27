from django.contrib import admin

from mypages.models import favgames, modslists, graphs, modeltimerecordscsvs, modeltotalhours

# Register your models here.

admin.site.register(favgames)
admin.site.register(modslists)
admin.site.register(graphs)
admin.site.register(modeltimerecordscsvs)
admin.site.register(modeltotalhours)

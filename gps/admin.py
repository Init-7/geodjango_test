from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Positions, Devices
# Register your models here.

admin.site.register(Positions, LeafletGeoAdmin)
admin.site.register(Devices, LeafletGeoAdmin)


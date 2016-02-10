from django.contrib.gis import admin
from .models import Positions
# Register your models here.

admin.site.register(Positions, admin.OSMGeoAdmin)

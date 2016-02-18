from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Planta, CentroNegocios, Trabajador, Riesgo, Zona, Rol

class GpsAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (-36.8282, -73.0514),
        'DEFAULT_ZOOM': 4,
    }

admin.site.register(Planta, GpsAdmin)
admin.site.register(CentroNegocios, LeafletGeoAdmin)
admin.site.register(Riesgo, LeafletGeoAdmin)
admin.site.register(Zona, LeafletGeoAdmin)
admin.site.register(Rol, LeafletGeoAdmin)
admin.site.register(Trabajador, LeafletGeoAdmin)

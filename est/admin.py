from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Planta, CentroNegocios, Trabajador, Riesgo, Zona, Rol, Empresa, Contacto, Salud, Estudios, Capacitacion

class GpsAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (-36.8282, -73.0514),
        'DEFAULT_ZOOM': 4,
    }

admin.site.register(Planta, GpsAdmin)
admin.site.register(CentroNegocios, GpsAdmin)
admin.site.register(Riesgo, GpsAdmin)
admin.site.register(Zona, GpsAdmin)
admin.site.register(Rol, GpsAdmin)
admin.site.register(Trabajador, GpsAdmin)
admin.site.register(Empresa, GpsAdmin)
admin.site.register(Contacto, GpsAdmin)
admin.site.register(Salud, GpsAdmin)
admin.site.register(Estudios, GpsAdmin)
admin.site.register(Capacitacion, GpsAdmin)

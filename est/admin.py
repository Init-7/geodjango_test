from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Planta, CentroNegocios, Trabajador, Riesgo, Zona, Rol

admin.site.register(Planta, LeafletGeoAdmin)
admin.site.register(CentroNegocios, LeafletGeoAdmin)
admin.site.register(Riesgo, LeafletGeoAdmin)
admin.site.register(Zona, LeafletGeoAdmin)
admin.site.register(Rol, LeafletGeoAdmin)
admin.site.register(Trabajador, LeafletGeoAdmin)

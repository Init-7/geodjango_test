from django.contrib.gis import admin

from .models import Planta, CentroNegocios, Trabajador, Riesgo, Zona, Rol, Empresa, Contacto, Salud, Estudios, Capacitacion, TrabajadorDevice, TrabajadorEstudios, TrabajadorCapacitacion


class CapacitacionInline(admin.TabularInline):
    model = TrabajadorCapacitacion
    extra = 1

class EstudiosInline(admin.TabularInline):
    model = TrabajadorEstudios
    extra = 1

class DevicesInline(admin.TabularInline):
    model = TrabajadorDevice
    extra = 1

class TrabajadorAdmin(admin.ModelAdmin):
    inlines = (CapacitacionInline,EstudiosInline, DevicesInline,)
    ordering = ('-tra_id',)


admin.site.register(Planta)
admin.site.register(CentroNegocios)
admin.site.register(Riesgo)
admin.site.register(Zona)
admin.site.register(Rol)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Empresa)
admin.site.register(Contacto)
admin.site.register(Salud)
admin.site.register(Estudios)
admin.site.register(Capacitacion)
admin.site.register(TrabajadorDevice)
admin.site.register(TrabajadorEstudios)
admin.site.register(TrabajadorCapacitacion)

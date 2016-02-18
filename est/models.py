from __future__ import unicode_literals

from django.contrib.gis.db import models

from gps.models import Devices

# Create your models here.

class Planta(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    empresa = models.CharField(max_length=128, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __unicode__(self):
        return u"%s %s" % (self.id, self.nombre)


class Riesgo(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    tipo = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.id, self.nombre)


class Zona(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    planta = models.ForeignKey(Planta)
    riesgo = models.ManyToManyField(Riesgo)
    zona = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return u"%s %s" % (self.id, self.nombre)


class CentroNegocios(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    planta = models.ForeignKey(Planta)
    codigo = models.CharField(max_length=24, blank=True, null=True)
    zonas = models.ManyToManyField(Zona)
    
    def __unicode__(self):
        return u"%s %s" % (self.id, self.nombre)


class Rol(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    zonas_permitidas = models.ManyToManyField(Zona)

    def __unicode__(self):
        return u"%s %s" % (self.id, self.nombre)


class Trabajador(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    rut = models.CharField(max_length=128, blank=True, null=True)
    centroNegocios = models.ForeignKey(CentroNegocios)
    rol = models.ManyToManyField(Rol)
    gps = models.ForeignKey(Devices, blank=True, null=True)
    supervisor = models.ForeignKey('Trabajador', blank=True, null=True)
    
    def __unicode__(self):
        return u"%s %s" % (self.id, self.nombre, self.centroNegocios)

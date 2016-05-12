from __future__ import unicode_literals

from django.contrib.gis.db import models

from gps.models import Devices

import qrcode
import StringIO

from django.core.urlresolvers import reverse  
from django.core.files.uploadedfile import InMemoryUploadedFile

#from qrcode.image.pure import PymagingImage

class Contacto (models.Model):
    nombre = models.CharField(max_length=128)
    fono = models.CharField(max_length=128,blank=True, null=True)
    e_mail = models.CharField(max_length=256, blank=True, null=True)
    nota = models.CharField(max_length=128, blank= True, null=True)

    def __unicode__(self):
        return u"%s %s %s" % (self.nombre, self.nota, self.fono)


class Empresa (models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    rut = models.CharField(max_length=128, blank=True, null=True)
    contacto = models.ForeignKey(Contacto, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.nombre)


class Planta(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.empresa)


class Riesgo(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    tipo = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.nombre)


class Zona(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    uso = models.CharField(max_length=128, blank=True, null=True)
    planta = models.ForeignKey(Planta, blank=True, null=True)
    riesgo = models.ManyToManyField(Riesgo, blank=True, null=True)
    zona = models.MultiPolygonField(srid=4326)
    nivel_riesgo = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.nombre)

class Tiempozona(models.Model):
	nombre = models.CharField(max_length=128, blank=True, null=True)
	horas =models.IntegerField(blank=True, null=True)
	minutos = models.IntegerField(blank=True, null=True)

class CentroNegocios(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    planta = models.ForeignKey(Planta, blank=True, null=True)
    codigo = models.CharField(max_length=24, blank=True, null=True)
    zonas = models.ManyToManyField(Zona, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s %s" % (self.codigo, self.nombre)


class Rol(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    zonas_permitidas = models.ManyToManyField(Zona, blank=True, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.id, self.nombre)


class Salud(models.Model):
    SALUD_CHOICES = (
        ('ALERGIA','Alergia'),
        ('ENFERMEDAD','Enfermedad'),
    )

    DETALLE_CHOICES = (
        ('PENICILINA','Penicilina'),
        ('POLVO','Polvo'),
        ('CIRROSIS','Cirrosis'),
        ('DIABETES','Diabetes'),
        ('CHOCOLATE','Chocolate'),
    )

    tipo = models.CharField(max_length=128, blank=True, null=True, choices=SALUD_CHOICES)
    detalle = models.CharField(max_length=128, blank=True, null=True, choices=DETALLE_CHOICES)
    observacion = models.CharField(max_length=2048, blank=True, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.tipo, self.detalle)

class Estudios(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    establecimiento = models.CharField(max_length=512, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=4096, blank=True, null=True)
   
    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.establecimiento)

class Capacitacion(models.Model):
    MODALIDAD_CHOICES = (
        ('PRESENCIAL','Presencial'),
        ('ON LINE','On Line'),
        ('MIXTO','Mixto')
    )

    nombre = models.CharField(max_length=512, blank=True, null=True)
    establecimiento = models.CharField(max_length=512, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=4096, blank=True, null=True)
    modalidad = models.CharField(max_length=128, blank=True, null=True, choices=MODALIDAD_CHOICES)
    horas = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.establecimiento)


class Trabajador(models.Model):
    
    TIPO_CONTACTO_CHOICES = (
        ('PADRE','Padre'),
        ('MADRE','Madre'),
        ('ESPOSO','Esposa(o)'),
        ('ABUELO','Abuelo(a)'),
        ('HIJO','Hijo(a)'),
        ('PAREJA','Pareja'),
        ('POLOLO','Pololo(a)')
    )

    nombre = models.CharField(max_length=128, blank=True, null=True)
    apellidop = models.CharField(max_length=128, blank=True, null=True)
    apellidom = models.CharField(max_length=128, blank=True, null=True)
    foto = models.ImageField(upload_to='avatar/', blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=256, blank=True, null=True)
#    contacto = models.ForeignKey(Contacto, blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    e_mail = models.CharField(max_length=128, blank=True, null=True)
    emergencia = models.ForeignKey(Contacto, blank=True, null=True)
    tipo_contacto = models.CharField(max_length=128, blank=True, null=True, choices=TIPO_CONTACTO_CHOICES)
    rut = models.CharField(max_length=128, blank=True, null=True)
    centroNegocios = models.ForeignKey(CentroNegocios, blank=True, null=True)
    cargo = models.CharField(max_length=128, blank=True, null=True)
    rol = models.ManyToManyField(Rol, blank=True, null=True)
    gps = models.ForeignKey(Devices, blank=True, null=True)
    supervisor = models.ForeignKey('Trabajador', blank=True, null=True)
    empresa = models.ForeignKey(Empresa, blank=True, null=True)
    salud = models.ManyToManyField(Salud, blank=True, null=True)
    estudios = models.ManyToManyField(Estudios, blank=True, null=True)      
    capacitacion = models.ManyToManyField(Capacitacion, blank=True, null=True)
    nivel_riesgo = models.IntegerField(blank=True, null=True)
    nota = models.CharField(max_length=256, blank=True, null=True)
    nota2 = models.CharField(max_length=256, blank=True, null=True)
    qrtext = models.CharField(max_length=256, blank=True, null=True)
    qrimg = models.ImageField(upload_to='qr/', blank=True, null=True)
 
#    def save(self, *args, **kwargs):
#        self.qrtext = "http://www.estchile.cl/cv/"+str(self.id)
#        qrimg = qrcode.make(self.qrtext)
#        qrimg.save("est/cv/img/qr/"+str(self.id)+".png", "PNG")
#        super(Trabajador, self).save(*args, **kwargs)
#
#

    def __unicode__(self):
        return u"%s %s %s %s %s" % (self.id, self.nombre, self.apellidop, self.apellidom, self.centroNegocios)

    def get_est_url(self):
        self.qrtext = "http://www.estchile.cl/cv/"+str(self.id)
        return self.qrtext

    def get_absolute_url(self):
        return reverse('est.views.card', args=[str(self.id)])

    def generate_qrimg(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data(self.get_absolute_url())
#        qr.add_data(self.get_est_url())
        qr.make(fit=True)

        img = qr.make_image()

        buffer = StringIO.StringIO()
        img.save(buffer)
        filename = 'trabajador-%s.png' % (self.id)
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.len, None)
        self.qrimg.save(filename, filebuffer)



from django.contrib.gis.db import models
from est.models import Zona

class Tiempozona(models.Model):

    def __init__(self,id, nombre, dias, horas, minutos, primero, ultimo, dif):
	self.id=id
	self.nombre = nombre
	self.dias = dias
	self.horas = horas
	self.minutos = minutos
        self.primero = primero
        self.ultimo = ultimo
        self.dif = dif

class Rangozona(object):

    def __init__(self, zona, inicio, fin):

        self.zona = zona
        self.inicio = inicio
        self.fin = fin 

class Listatrabajadores(models.Model):
    
    def __init__( self):
        self.nombre = None
	self.id = None

class Listaplantas(models.Model):

    def __init__(self, id, nombre):
	self.id = id
	self.nombre=nombre

class Listacn(models.Model):

    def __init__(self):
	self.nombre= None
	self.id= None	




from django.contrib.gis.db import models
from est.models import Zona

class Tiempozona(object):

    def __init__(self, nombre, dias, horas, minutos, primero, ultimo, dif):

	self.nombre = nombre
	self.dias = dias
	self.horas = horas
	self.minutos = minutos
        self.primero = primero
        self.ultirmo = ultimo
        self.dif = dif

class Rangozona(object):

    def __init__(zona, inicio, fin):

        self.zona = zona
        self.inicio = inicio
        self.fin = fin 

class Listatrabajadores(object):
    
    def __init__(nombre):
        self.nombre = nombre

class Listaplantas(object):

    def __init__(nombre):
	self.nombre= nombre	

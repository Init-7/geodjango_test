# -*- encoding: utf-8 -*-
from django.shortcuts import render

from django.core import serializers
from djgeojson.serializers import Serializer as GeoJSONSerializer

from django.http import HttpResponse

from est.models import Planta, Zona, Trabajador, CentroNegocios,Tiempozona
from gps.models import Positions, Devices, Posicionestrabajador
from itertools import chain
from datetime import datetime
from djgeojson.views import GeoJSONResponseMixin

from django.core.serializers.python import Serializer

#Serialiser copy paste
class MySerialiser(Serializer):
    def end_object( self, obj ):
        self._current['id'] = obj._get_pk_val()
        self.objects.append( self._current )


def last_five(request):
#Ultimas 5 posiciones registradas
    last_five = Positions.objects.order_by('-id')[:5]
    
    data = serializers.serialize('json', last_five)
    
    return HttpResponse(data, content_type='application/json')

def infoplantas(request):
	pl= Planta.objects.all()
	contenidos=[]

        serializer = MySerialiser()

	for p in pl:
		contenidos.append(p)
        data = serializers.serialize('json', contenidos, fields=('nombre'))
#        data = serializer.serialize(contenidos)
	return HttpResponse(data, content_type='application/json')



def planta(request, planta):
#Posiciones registradas dentro de una determinada planta    
    pl = Planta.objects.get(nombre = planta)

    contenidos = []

    for d in Devices.objects.all():
        p = Positions.objects.get(id = d.positionid)
        if(pl.geom.contains(p.geom)):
            contenidos.append(p)


#    for p in puntos:
#        if(pl.geom.contains(p.geom)):
#            contenidos.append(p)

#    data = serializers.serialize('json', contenidos)
    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data)#, content_type='application/json')

def centro(request, planta, centro):

    tcn = Trabajador.objects.filter(centroNegocios__id = centro)

    contenidos = []

    for tr in tcn:
        if tr.gps_id:
#        t = Trabajador.objects.get(id=trabajador) #Trabajadores con el id solicitado
            dev = Devices.objects.get(id=tr.gps_id) #Dispositivo correspondiente al trabajador
            punto = Positions.objects.get(id = dev.positionid)
	auxiliar=Posicionestrabajador()	
	auxiliar.lat=punto.lat	
	auxiliar.lon=punto.lon
	auxiliar.address=punto.address
	auxiliar.fixtime=punto.fixtime	
	
	auxiliar.nombre=tr.nombre
	auxiliar.apellidop=tr.apellidop
	auxiliar.apellidom=tr.apellidom
	auxiliar.fecha_nac=tr.fecha_nac
	#auxiliar.estudios=t.estudios
	auxiliar.rut=tr.rut
	auxiliar.nivel_riesgo=tr.nivel_riesgo
	auxiliar.direccion=tr.direccion
	#auxiliar.centroNegocios=t.centroNegocios
	#auxiliar.gps=t.gps
	contenidos.append(auxiliar)

    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data)#, content_type='application/json')



def trabajador(request, trabajador):
#Ultima posicion de un trabajador     
	t = Trabajador.objects.get(id=trabajador) #Trabajadores con el id solicitado
	dev = Devices.objects.get(id=t.gps_id) #Dispositivo correspondiente al trabajador
	punto = Positions.objects.get(id = dev.positionid) #Grupo de puntos relacionados a un trabajador
		
	contenidos = []

	#puntos = Positions.objects.raw('SELECT * FROM Devices as d join Positions as p on p."deviceId"=d.id join "Trabajador" as t on d.id=t.gps_id where t.id=%s ', [trabajador])
	
	#for p in puntos:	
	auxiliar=Posicionestrabajador()	
	auxiliar.lat=punto.lat	
	auxiliar.lon=punto.lon
	auxiliar.address=punto.address
	auxiliar.fixtime=punto.fixtime	
	
	auxiliar.nombre=t.nombre
	auxiliar.apellidop=t.apellidop
	auxiliar.apellidom=t.apellidom
	auxiliar.fecha_nac=t.fecha_nac
	#auxiliar.estudios=t.estudios
	auxiliar.rut=t.rut
	auxiliar.nivel_riesgo=t.nivel_riesgo
	auxiliar.direccion=t.direccion
	#auxiliar.centroNegocios=t.centroNegocios
	#auxiliar.gps=t.gps
	contenidos.append(auxiliar)
		
	data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)

	return HttpResponse(data)#, content_type='application/json')

def tiempoplanta(request, planta, fechainicio, fechafin):
#Posiciones registradas en una determinada planta, durante un rango de tiempo (fecha)
	pl = Planta.objects.get(nombre = planta)

	posiciones = Positions.objects.filter(fixtime__range=[fechainicio,fechafin])
	contenidos = []
	for p in posiciones:
		if(pl.geom.contains(p.geom)):
			contenidos.append(p)			
	
	data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)
	return HttpResponse(data)

def tiempoplantaconhoras(request, planta, fechainicio, fechafin):
#Posiciones registradas en una determinada planta, durante un rango de tiempo (fecha,hora)
	
    	pl = Planta.objects.get(nombre = planta)	
	
	posiciones = Positions.objects.filter(fixtime__range=[fechainicio,fechafin])
	contenidos = []
	for p in posiciones:
		if(pl.geom.contains(p.geom)):
			contenidos.append(p)		
	
	data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)
	return HttpResponse(data)

def lugarestrabajador(request, trabajador,planta, fechainicio, fechafin):
#Posiciones de un trabajador de la planta en un rango de tiempo
	cn =CentroNegocios.filter()
    	pl = Planta.objects.get(nombre = planta)
	
	posiciones = Positions.objects.filter(fixtime__range=[fechainicio,fechafin])
        t = Trabajador.objects.get(id=trabajador) #Trabajadores con el id solicitado
	dev = Devices.objects.get(id=t.gps_id) #Dispositivo correspondiente al trabajador
	posiciones = Positions.objects.filter(deviceid=dev)
	contenidos = []
	for p in posiciones:
		if(pl.geom.contains(p.geom)):
			contenidos.append(p)						
	
	data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)
	return HttpResponse(data)

def datosinforme(request,cnegocios, trabajador,planta, fechainicio, fechafin):
#Posiciones de un trabajador de la planta en un rango de tiempo
	
    	pl = Planta.objects.get(nombre = planta)
	zonas= Zona.objects.filter(planta__nombre=planta)
	posiciones = Positions.objects.filter(fixtime__range=[fechainicio,fechafin])
        t = Trabajador.objects.get(id=trabajador) #Trabajadores con el id solicitado
	dev = Devices.objects.get(id=t.gps_id) #Dispositivo correspondiente al trabajador
	posiciones = Positions.objects.filter(deviceid=dev)
	contenidos = []
	tiempozonas = []
	posicioneszona =[]
	contenidozona=[]	

	for i, z in enumerate(zonas): #Para cada una de las zonas en una planta
		contenidozona=[]
		for p in posiciones: #Para cada una de las posiciones
			if(z.zona.contains(p.geom)): #Si la posicion se encuentra en una zona
				contenidozona.append(p)
		if(contenidozona):		
			pr=contenidozona[0].fixtime
			ul=contenidozona[-1].fixtime
			tiempozona=pr-ul
			obj=Tiempozona()
			obj.nombre=z.nombre
			obj.horas=abs(tiempozona.seconds/3600)
			obj.minutos=abs((tiempozona.seconds - abs(tiempozona.seconds/3600)*3600)/60)
			contenidos.append(obj)
		else:
			obj=Tiempozona()
			obj.nombre=z.nombre
			obj.horas=0
			obj.minutos=0
			contenidos.append(obj)

	#for i,z in enumerate(zonas):
	#	pr=posicioneszona[i].first().fixtime
	#	ul=posicioneszona[i].last().fixtime
	#	dif=pr-ul
	#	contenidos.append(dif)	
			
	#primero= posiciones.first().fixtime
	#ultimo= posiciones.last().fixtime
	#total=ultimo-primero
	
	#dias=diferencia.days
	#horas=diferencia.

	data = serializers.serialize('json', contenidos)
	return HttpResponse(data, content_type='application/json')

def riesgotrabajador(request, planta, nro):
#Posiciones de trabajadores con mayor riesgo
    	
	pl = Planta.objects.get(nombre = planta)
	tr = Trabajador.objects.order_by('-nivel_riesgo')[:nro]
	contenidos = []
	
	for t in tr:
		dev = Devices.objects.get(id=t.gps_id) #Dispositivo correspondiente al trabajador
		punto = Positions.objects.get(id = dev.positionid) #Grupo de puntos relacionados a un trabajador
       		if(pl.geom.contains(punto.geom)):
			auxiliar=Posicionestrabajador()
			auxiliar.lat=punto.lat	
			auxiliar.lon=punto.lon
			auxiliar.address=punto.address
			auxiliar.fixtime=punto.fixtime	
	
			auxiliar.nombre=t.nombre
			auxiliar.apellidop=t.apellidop
			auxiliar.apellidom=t.apellidom
			auxiliar.fecha_nac=t.fecha_nac
			#auxiliar.estudios=t.estudios
			auxiliar.rut=t.rut
			auxiliar.nivel_riesgo=t.nivel_riesgo
			auxiliar.direccion=t.direccion
			#auxiliar.centroNegocios=t.centroNegocios
			#auxiliar.gps=t.gps
			contenidos.append(auxiliar)									
	
	data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)
	return HttpResponse(data)


def curriculum(request, trabajador):

    data = Trabajador.objects.get(id=trabajador)

    context = {'data': data}

    return render(request,'cv/cv.html', context)

#    return render(request, '../templates/curriculum/classic.html', {
#        'resume': resume,
#        'skills': resume.skills.order_by('category', '-weight'),
#        'projects': resume.projects.order_by('-weight'),
#        'experiences': resume.experiences.order_by('-start_year'),
#        'trainings': resume.trainings.order_by('-year', '-month'),
#        'certifications': resume.certifications.order_by('-start_year', '-start_month')
#    })
#
#

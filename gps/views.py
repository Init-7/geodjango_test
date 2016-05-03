# -*- encoding: utf-8 -*-
from django.shortcuts import render

from django.core import serializers
from djgeojson.serializers import Serializer as GeoJSONSerializer

from django.http import HttpResponse

from est.models import Planta, Zona, Trabajador, CentroNegocios
from gps.models import Positions, Devices

from djgeojson.views import GeoJSONResponseMixin

def last_five(request):
    last_five = Positions.objects.order_by('-id')[:5]
    
    data = serializers.serialize('json', last_five)
    
    return HttpResponse(data, content_type='application/json')


def planta(request, planta):
    puntos = Positions.objects.all()
    pl = Planta.objects.get(nombre = planta)

    contenidos = []

    for d in Devices.objects.all():
        p = Positions.objects.get(id =d.positionid)
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
            contenidos.append(punto)

    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data)#, content_type='application/json')



def trabajador(request, planta, centro, trabajador):
    t = Trabajador.objects.get(id=trabajador) #Trabajadores con el id solicitado
    dev = Devices.objects.get(id=t.gps_id) #Dispositivo correspondiente al trabajador
    punto = Positions.objects.get(id = dev.positionid)

    contenidos = []
    contenidos.append(punto)

    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data)#, content_type='application/json')


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

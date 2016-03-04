# -*- encoding: utf-8 -*-
from django.shortcuts import render

#from django.core import serializers
from djgeojson.serializers import Serializer as GeoJSONSerializer

from django.http import HttpResponse

from est.models import Planta, Zona, Trabajador, CentroNegocios
from gps.models import Positions, Devices

from djgeojson.views import GeoJSONResponseMixin

def positions(request):
    last_five = Positions.objects.order_by('-id')[:5]
    
    data = serializers.serialize('json', last_five)
    
    return HttpResponse(data, content_type='application/json')


#def detail(request, question_id):
#    return HttpResponse("esta es la pregunta numero %s." % question_id)
#
#def results(request, question_id):
#    response = "Este es el resultado de la pregunta %s"
#    return HttpResponse(response % question_id)
#
#def vote(request, question_id):
#    return HttpResponse("Estas votando en la pregunta %s." % question_id)

def planta(request, planta):
    puntos = Positions.objects.all()
    pl = Planta.objects.get(nombre = planta)
    
    contenidos = []

    for p in puntos:
        if(pl.geom.contains(p.geom)):
            contenidos.append(p)

#    data = serializers.serialize('json', contenidos)
    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data)#, content_type='application/json')
#    return GeoJSONResponseMixin(data)

#def curriculum(request, trabajador):
#
#    data = Trabajador.objects.get(id=trabajador)
#
#    context = {'data': data}
#
#    return render(request,'cv/cv.html', context)
#
#    return render(request, '../templates/curriculum/classic.html', {
#        'resume': resume,
#        'skills': resume.skills.order_by('category', '-weight'),
#        'projects': resume.projects.order_by('-weight'),
#        'experiences': resume.experiences.order_by('-start_year'),
#        'trainings': resume.trainings.order_by('-year', '-month'),
#        'certifications': resume.certifications.order_by('-start_year', '-start_month')
#    })

#def centro(request, planta, centro):
#    puntos = Positions.objects.all()
#    pl = Planta.objects.get(nombre = planta)
#    cn = CentroNegocios.get(nombre= centro)
#
#    contenidos = []
#
#    for p in puntos:
#        if(pl.geom.contains(p.geom)):
#            contenidos.append(p)
#
#    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)
#
#    return HttpResponse(data)#, content_type='application/json')
#
#
#def trabajador(request, planta, centro, trabajador):
#    puntos = Positions.objects.all()
#    pl = Planta.objects.get(nombre = planta)
#    cn = CentroNegocios.objects.get(id = centro)    
#
#    contenidos = []
#
#    Trabajador.objects.filer(device_id=)
#
#
##    for in cn:
    #    for p in puntos:
    #        if(pl.geom.contains(p.geom)):
    #            contenidos.append(p)
#
#    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)
#
#    return HttpResponse(data)#, content_type='application/json')
#

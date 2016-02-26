from django.shortcuts import render

#from django.core import serializers
from djgeojson.serializers import Serializer as GeoJSONSerializer

from django.http import HttpResponse

from est.models import Planta, Zona, Trabajador
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

def puntos(request, planta):
    puntos = Positions.objects.all()
    pl = Planta.objects.get(nombre = planta)
    
    contenidos = []

    for p in puntos:
        if(pl.geom.contains(p.geom)):
            contenidos.append(p)

#    data = serializers.serialize('json', contenidos)
    data = GeoJSONSerializer().serialize(contenidos, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data, content_type='application/json')
#    return GeoJSONResponseMixin(data)

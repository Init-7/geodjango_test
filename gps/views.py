from django.shortcuts import render

from gps.models import Positions

from django.core import serializers

from django.http import HttpResponse


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

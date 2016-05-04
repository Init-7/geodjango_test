from django.shortcuts import render

from est.models import Planta, Zona, Trabajador, CentroNegocios

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

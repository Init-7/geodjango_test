from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cv/(?P<trabajador>[\w]+)/$' ,views.curriculum, name='curriculum'),
    url(r'^card/(?P<trabajador>[\w]+)/$' ,views.card, name='card'),
]

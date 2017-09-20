from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cv/(?P<trabajador>[0-9]+)/$' ,views.curriculum, name='curriculum'),
    url(r'^card/(?P<trabajador>[0-9]+)/$' ,views.card, name='card'),
]

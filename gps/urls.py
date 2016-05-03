from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from . import views

from djgeojson.views import GeoJSONLayerView

from .models import Positions

urlpatterns = [
#URL que entrega las ultimas 5 posiciones en Json normal
    url(r'^positions$', views.last_five, name='positions'),
#URL que entrega un mapa leaflet con todos los puntos de posiciones
    url(r'^$', TemplateView.as_view(template_name='gps/index.html'), name='home'),
#URL que entrega un GeoJSON de todas las posiciones
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Positions), name='data'),
#    url(r'^positions.leaftlet$', views.positions, name='positions')
    url(r'^(?P<planta>[\w]+)/puntos/$',views.planta, name='planta'),
    url(r'^(?P<planta>[\w]+)/(?P<centro>[0-9]+)/puntos/$',views.centro, name='centro'),
    url(r'^(?P<planta>[\w]+)/(?P<centro>[0-9]+)/(?P<trabajador>[0-9]+)/puntos/$',views.trabajador, name='trabajador'),
#    url(r'^cv/(?P<trabajador>[0-9]+)/$' ,views.curriculum, name='curriculum'),
]

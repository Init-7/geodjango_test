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
    url(r'^trabajador/(?P<trabajador>[0-9]+)/$',views.trabajador, name='trabajador'), # Se elimina la palabra "puntos" para evitar procesar consulta anterior
    url(r'^plantas/$',views.listaplantas, name='plantas'),
    url(r'^(?P<nombreplanta>[\w]+)/trabajadores/$',views.trabajadoresplanta, name='trabajadoresplanta'),
    url(r'^(?P<planta>[\w]+)/(?P<fechainicio>(\d{4})[/.-](\d{2})[/.-](\d{2}))/(?P<fechafin>(\d{4})[/.-](\d{2})[/.-](\d{2}))/puntos/$',views.tiempoplanta, name='doc'),
    url(r'^(?P<planta>[\w]+)/(?P<fechainicio>(\d{4})[/.-](\d{2})[/.-](\d{2})[/.\s](\d{2})[/.:](\d{2}))/(?P<fechafin>(\d{4})[/.-](\d{2})[/.-](\d{2})[/.\s](\d{2})[/.:](\d{2}))/puntos/$',views.tiempoplantaconhoras, name='doc'),
    url(r'^(?P<planta>[\w]+)/(?P<trabajador>[\w]+)/(?P<fechainicio>(\d{4})[/.-](\d{2})[/.-](\d{2}))/(?P<fechafin>(\d{4})[/.-](\d{2})[/.-](\d{2}))/$',views.lugarestrabajador, name='centro'),
    url(r'^(?P<planta>[\w]+)/ranking_riesgo/(?P<nro>[0-9]+)/$',views.riesgotrabajador),
    url(r'^plantas.json/$',views.infoplantas),
    url(r'^datosinforme/(?P<planta>[\w]+)/(?P<cnegocios>[\w]+)/(?P<trabajador>[\w]+)/(?P<fechainicio>(\d{4})[/.-](\d{2})[/.-](\d{2}))/(?P<fechafin>(\d{4})[/.-](\d{2})[/.-](\d{2}))/$',views.datosinforme),
#    url(r'^cv/(?P<trabajador>[0-9]+)/$' ,views.curriculum, name='curriculum'),
]

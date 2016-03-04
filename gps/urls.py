from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from . import views

from djgeojson.views import GeoJSONLayerView

from .models import Positions

urlpatterns = [
    url(r'^positions$', views.last_five, name='positions'),
#    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
#    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^$', TemplateView.as_view(template_name='gps/index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Positions), name='data'),
#    url(r'^positions.leaftlet$', views.positions, name='positions')
    url(r'^(?P<planta>[\w]+)/puntos/$',views.planta, name='planta'),
#    url(r'^cv/(?P<trabajador>[0-9]+)/$' ,views.curriculum, name='curriculum')
    url(r'^(?P<planta>[\w]+)/(?P<centro>[0-9]+)/puntos/$',views.centro, name='centro'),
    url(r'^(?P<planta>[\w]+)/(?P<centro>[0-9]+)/(?P<trabajador>[0-9]+)/puntos/$',views.trabajador, name='trabajador'),
]

from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from . import views

from djgeojson.views import GeoJSONLayerView

from .models import Positions

urlpatterns = [
    url(r'^positions$', views.positions, name='positions'),
#    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
#    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^$', TemplateView.as_view(template_name='gps/index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Positions), name='data'),
#    url(r'^positions.leaftlet$', views.positions, name='positions')

    url(r'^(?P<planta>[\w]+)/puntos/$',views.puntos, name='puntos'),

]

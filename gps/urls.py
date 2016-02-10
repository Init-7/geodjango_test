from django.conf.urls import url

from . import views

from djgeojson.views import GeoJSONLayerView

from .models import Positions

urlpatterns = [
    url(r'^positions$', views.positions, name='positions'),
#    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
#    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Positions), name='data'),
]

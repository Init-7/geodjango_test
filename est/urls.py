from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^cv/(?P<trabajador>[0-9]+)/$' ,views.curriculum, name='curriculum'),
]

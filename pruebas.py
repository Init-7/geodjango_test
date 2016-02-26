from est.models import Planta, Zona, Trabajador
from gps.models import Positions, Devices

puntos = Positions.objects.all()
plantas = Planta.objects.all()

for p in puntos:
    if(pl.geom.contains(p.geom)):
        print(p.geom.geojson)

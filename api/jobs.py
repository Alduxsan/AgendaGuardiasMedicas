from django.db import models
from Aplicaciones.Agenda.models import Guardia
import datetime



def guardia_ranking_update():

  print("===== SE HA INICIADO APScheduler =====")
  guardias = Guardia.objects.filter(disponible=True)
  
  for guardia in guardias:
       if guardia.min_ranking < 200:
         print(f"\nLa guardia {guardia.id} tiene un valor de ranking de: {guardia.min_ranking} {datetime.datetime.now()}")
         guardia.min_ranking += 1
         print(f"La guardia {guardia.id} cambio su ranking al nro: {guardia.min_ranking}")
         guardia.save()  
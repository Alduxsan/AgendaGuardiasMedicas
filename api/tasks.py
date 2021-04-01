 
from Aplicaciones.Agenda.models import Guardia

@shared_task    
def guardia_ranking_update():

  print("PROBANDO CELERY BEATS "*20)
  guardias = Guardia.objects.filter(disponible=True)
  for guardia in guardias:
       if guardia.min_ranking < 200:
           guardia.min_ranking =+ 1
           guardia.save()  


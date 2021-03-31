from Aplicaciones.Agenda.models import Guardia

def guardia_ranking_update():
  print("CRONTAB ESTA FUNCIONANDO")
  # guardias = Guardia.objects.filter(disponible=True)
  # for guardia in guardias:
  #     if guardia.min_ranking < 200:
  #         guardia.min_ranking =+ 1
  #         guardia.save()  

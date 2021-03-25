from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Aplicaciones.Agenda.models import *
from . import serializers

class GuardiasApiView(APIView):
    
    serializer_class = serializers.GuardiaSerializer

    def get(self, request):

        allGuardias = Guardia.object.all().values()

        return Response({"Guardias":"Lista de guardias: ", "Guardias":allGuardias})

    def post(self, request):

        serializer = serializers.GuardiaSerializer(data = request.data)

        if serializer.is_valid():

            Guardia.object.create(
            title = request.data['fecha'],
            turno = request.data['turno'],
            centroSalud = request.data['centroSalud'],
            medico = request.data['medico'],
            usuario = request.data['usuario'],
            disponible = request.data['disponible']
            )

            allGuardias = Guardia.object.all().values()
            return Response({"Guardias":"Lista de guardias: ", "Guardias":allGuardias})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

   
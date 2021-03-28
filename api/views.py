from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from Aplicaciones.Agenda.models import Guardia
from api.serializers import GuardiaSerializer
from api import serializers

class GuardiasApiView(APIView):
    
    serializer_class = GuardiaSerializer()

    def get(self, request):

        allGuardias = Guardia.objects.all().values()

        return Response({"Guardias":"Lista de guardias: ", "guardias": allGuardias})

    def post(self, request):

        serializer = serializers.GuardiaSerializer(data = request.data)

        if serializer.is_valid():

            Guardia.objects.create(
            title = request.data['fecha'],
            turno = request.data['turno'],
            centroSalud = request.data['centroSalud'],
            medico = request.data['medico'],
            usuario = request.data['usuario'],
            disponible = request.data['disponible']
            )

            allGuardias = Guardia.objects.all().values()
            return Response({"Guardias":"Lista de guardias: ", "guardias":allGuardias})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class GuardiasViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

    
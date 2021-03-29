from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, viewsets
from Aplicaciones.Agenda.models import Guardia, Medico
from api.serializers import GuardiaSerializer, MedicoSerializer
from api import serializers
from rest_framework.decorators import action
from django.contrib.auth.models import User

class GuardiasViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

    def list(self, request):
        
        queryset = Guardia.objects.filter(disponible=True)
        serializer = GuardiaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        mis_guardias = Guardia.objects.filter(medico = params['pk'])
        serializer = GuardiaSerializer(mis_guardias, many=True)
        return Response(serializer.data)

class Guardia_modificar(viewsets.ModelViewSet):

    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

    def put(self, request, *args, **kwargs):
        '''actualiza solo los campos indicados de la instancia'''
        return self.partial_update(request, *args, **kwargs)

class Medico_Datos(viewsets.ModelViewSet):

    serializer_class = serializers.MedicoSerializer
    queryset = Medico.objects.all()

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        medico_user = Medico.objects.filter(ci = params['pk'])
        serializer = MedicoSerializer(medico_user, many=True)
        return Response(serializer.data)

from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from Aplicaciones.Agenda.models import Guardia, Medico
from . import serializers
from .serializers import GuardiaSerializer, MedicoSerializer


class GuardiasViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

    def list(self, request):

        user = request.user
        #medico = Medico.objects.filter(User.username == user.username)
        queryset = Guardia.objects.filter(disponible=True, min_ranking__gte = 2)
        serializer = GuardiaSerializer(queryset, many=True)
        return Response(serializer.data)

class MisGuardias(viewsets.ModelViewSet):
    
    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

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

class  MartyMcFly(viewsets.ModelViewSet):

    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

    def list(self, request):
        
        queryset = Guardia.objects.filter(disponible=True)

        for guardia in queryset:
            guardia.min_ranking = 1
            guardia.save()
        
        queryset = Guardia.objects.filter(disponible=True)
        serializer = GuardiaSerializer(queryset, many=True)
        return Response(serializer.data)   


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


"""
{"username":"medico_uno","password":"adelante"}
"""

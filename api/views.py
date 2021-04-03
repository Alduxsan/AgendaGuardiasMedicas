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

    def list(self, request, *args, **kwargs):
 
        user = request.user
        medico = Medico.objects.get(usuario = user)
        ranking_medico = medico.ranking
        departamento_medico = medico.departamento
        queryset = Guardia.objects.filter(

            disponible=True, 
            departamento=departamento_medico, 
            min_ranking__gte = ranking_medico)

        serializer = GuardiaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        guardias_departamento = Guardia.objects.filter(id = params['pk'])
        serializer = GuardiaSerializer(guardias_departamento, many=True)
        return Response(serializer.data)

class GuardiasFiltro(viewsets.ModelViewSet):

    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

    def list(self, request):
 
        lista_dept = request.query_params['dep'].split('-')
        guardias_departamento = Guardia.objects.filter(departamento__in = lista_dept, disponible=True)
        serializer = GuardiaSerializer(guardias_departamento, many=True)
        return Response(serializer.data)
        
class MisGuardias(viewsets.ModelViewSet):
    
    serializer_class = serializers.GuardiaSerializer
    queryset = Guardia.objects.all()

    def list(self, request, *args, **kwargs):
 
        user = request.user
        medico = Medico.objects.get(usuario = user)
        ci_medico = medico.ci
        
        queryset = Guardia.objects.filter(

            medico = ci_medico

        )

        serializer = GuardiaSerializer(queryset, many=True)
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
    
    def list(self, request):
        medico = Medico.objects.filter(usuario = request.user)
        serializer = MedicoSerializer(medico, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        '''actualiza solo los campos indicados de la instancia'''
        return self.partial_update(request, *args, **kwargs)
    
class  MartyMcFly(viewsets.ModelViewSet):
    '''Modifica el valor de ranking_min de todas las guardias'''
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


        #{"username":"medico_uno","password":"adelante"}
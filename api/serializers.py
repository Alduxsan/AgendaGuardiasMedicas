from rest_framework import serializers
from Aplicaciones.Agenda.models import *
from Aplicaciones.Cuentas.models import *
from django.contrib.auth.models import User

from Aplicaciones.Agenda.models import Guardia, Medico

class GuardiaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Guardia
        fields = "__all__"

    def create(self, validated_data):
        guardia = Guardia(nombre=validated_data.get("nombre"))
        guardia.save()
        return validated_data


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Medico
        fields = "__all__"

    
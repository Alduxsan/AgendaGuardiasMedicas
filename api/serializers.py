from rest_framework import serializers
from Aplicaciones.Agenda.models import *


class GuardiaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Guardia
        fields = "__all__"

    def create(self, validated_data):
        guardia = Guardia(nombre=validated_data.get("nombre"))
        guardia.save()
        return validated_data

    
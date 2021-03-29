from rest_framework import serializers
from Aplicaciones.Agenda.models import Guardia, Medico

class GuardiaSerializer(serializers.ModelSerializer):

    class Meta:
        model= Guardia
        fields = "__all__"

    def create(self, validated_data):

        guardia = Guardia(

            fecha = validated_data['fecha'],
            turno = validated_data['turno'],
            centroSalud = validated_data['centroSalud']
        )
        
        guardia.save()
        return guardia
        

class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Medico
        fields = "__all__"


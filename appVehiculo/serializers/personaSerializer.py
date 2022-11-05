from rest_framework import serializers
from appVehiculo.models.persona import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

from rest_framework import serializers
from appVehiculo.models.envio import Envio


class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'

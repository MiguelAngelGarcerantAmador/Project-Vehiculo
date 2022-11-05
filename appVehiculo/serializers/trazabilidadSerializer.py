from rest_framework import serializers
from appVehiculo.models.trazabilidad import Trazabilidad


class TrazabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trazabilidad
        fields = '__all__'

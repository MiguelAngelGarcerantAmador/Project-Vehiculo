from rest_framework import serializers

from appVehiculo.models.vehiculo import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = "__all__"

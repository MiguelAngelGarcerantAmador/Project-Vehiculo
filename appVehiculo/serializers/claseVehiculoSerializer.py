from rest_framework import serializers
from appVehiculo.models.claseVehiculo import ClaseVehiculo


class ClaseVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaseVehiculo
        fields = "__all__"

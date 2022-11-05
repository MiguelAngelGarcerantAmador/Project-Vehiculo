from rest_framework import serializers
from appVehiculo.models.tipoVehiculo import TipoVehiculo


class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'

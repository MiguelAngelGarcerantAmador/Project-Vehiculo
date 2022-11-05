from rest_framework import serializers
from appVehiculo.models.ordenCompra import OrdenCompra


class OrdenCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenCompra
        fields = '__all__'

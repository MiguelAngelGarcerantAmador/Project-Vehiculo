from rest_framework import serializers

from appVehiculo.models.tipoPago import TipoPago


class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields = "__all__"

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from appVehiculo.models.tipoPago import TipoPago
from appVehiculo.serializers.tipoPagoSerializer import TipoPagoSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def gestionTipoPago(request):
    if request.method == "GET":
        datos_tipopago = TipoPago.objects.all()
        serializer_tipopago = TipoPagoSerializer(datos_tipopago, many=True)
        return Response(serializer_tipopago.data)

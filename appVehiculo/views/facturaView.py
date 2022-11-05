from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from appVehiculo.models.factura import Factura
from appVehiculo.serializers.facturaSerializer import FacturaSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gestionFactura(request):
    if request.method == 'GET':
        datos_factura = Factura.objects.all()
        serializer_factura = FacturaSerializer(
            datos_factura, many=True)
        return Response(serializer_factura.data)

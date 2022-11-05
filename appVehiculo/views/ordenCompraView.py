from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from appVehiculo.models.ordenCompra import OrdenCompra
from appVehiculo.serializers.ordenCompraSerializer import OrdenCompraSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gestionOrdenCompra(request):
    if request.method == 'GET':
        datos_ordencompra = OrdenCompra.objects.all()
        serializer_ordencompra = OrdenCompraSerializer(datos_ordencompra, many=True)
        return Response(serializer_ordencompra.data)

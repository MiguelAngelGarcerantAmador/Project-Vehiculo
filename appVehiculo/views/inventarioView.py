from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from appVehiculo.models.inventario import Inventario
from appVehiculo.serializers.inventarioSerializer import InventarioSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gestionInventario(request):
    if request.method == 'GET':
        datos_inventario = Inventario.objects.all()
        serializer_inventario = InventarioSerializer(
            datos_inventario, many=True)
        return Response(serializer_inventario.data)

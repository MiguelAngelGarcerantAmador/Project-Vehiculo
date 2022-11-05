from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from appVehiculo.models.trazabilidad import Trazabilidad
from appVehiculo.serializers.trazabilidadSerializer import TrazabilidadSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gestionTrazabilidad(request):
    if request.method == 'GET':
        datos_trazabilidad = Trazabilidad.objects.all()
        serializer_trazabilidad = TrazabilidadSerializer(
            datos_trazabilidad, many=True)
        return Response(serializer_trazabilidad.data)

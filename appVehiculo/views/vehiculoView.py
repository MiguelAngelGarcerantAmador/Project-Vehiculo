from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from appVehiculo.models.vehiculo import Vehiculo
from appVehiculo.serializers.vehiculoSerializer import VehiculoSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def gestionVehiculo(request):
    if request.method == "GET":
        datos_vehiculo = Vehiculo.objects.all()
        serializer_vehiculo = VehiculoSerializer(datos_vehiculo, many=True)
        return Response(serializer_vehiculo.data)

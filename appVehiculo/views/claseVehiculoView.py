from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from appVehiculo.models.claseVehiculo import ClaseVehiculo
from appVehiculo.serializers.claseVehiculoSerializer import ClaseVehiculoSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def gestionClaseVehiculo(request):
    if request.method == "GET":
        datos_clasevehiculo = ClaseVehiculo.objects.all()
        serializer_clasevehiculo = ClaseVehiculoSerializer(
            datos_clasevehiculo, many=True
        )
        return Response(serializer_clasevehiculo.data)

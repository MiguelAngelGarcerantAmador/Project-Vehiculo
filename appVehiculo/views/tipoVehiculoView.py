from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from appVehiculo.models.tipoVehiculo import TipoVehiculo
from appVehiculo.serializers.tipoVehiculoSerializer import TipoVehiculoSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def gestionTipoVehiculo(request):
    if request.method == "GET":
        datos_tipovehiculo = TipoVehiculo.objects.all()
        serializer_tipovehiculo = TipoVehiculoSerializer(datos_tipovehiculo, many=True)
        return Response(serializer_tipovehiculo.data)

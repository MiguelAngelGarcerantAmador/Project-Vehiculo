from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from appVehiculo.models.envio import Envio
from appVehiculo.serializers.envioSerializer import EnvioSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gestionEnvio(request):
    if request.method == 'GET':
        datos_envio = Envio.objects.all()
        serializer_envio = EnvioSerializer(
            datos_envio, many=True)
        return Response(serializer_envio.data)

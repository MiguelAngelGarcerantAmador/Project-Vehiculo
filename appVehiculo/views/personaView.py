from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from appVehiculo.models.persona import Persona
from appVehiculo.serializers.personaSerializer import PersonaSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def gestionPersona(request):
    if request.method == "GET":
        datos_persona = Persona.objects.all()
        serializer_persona = PersonaSerializer(datos_persona, many=True)
        return Response(serializer_persona.data)

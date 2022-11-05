from django.db import models

from .claseVehiculo import ClaseVehiculo
from .tipoVehiculo import TipoVehiculo


class Vehiculo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    marca = models.CharField(max_length=40)
    modelo_vehiculo = models.CharField(max_length=30)
    año_modelo = models.CharField(max_length=5)
    num_pasajeros = models.CharField(max_length=3)
    color = models.CharField(max_length=30)
    matricula = models.CharField(max_length=8)
    clases_servicios = models.CharField(max_length=40)
    kilometraje = models.CharField(max_length=40)
    cilindraje = models.CharField(max_length=40)
    clase_vehiculo = models.ForeignKey(ClaseVehiculo, on_delete=models.CASCADE)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)

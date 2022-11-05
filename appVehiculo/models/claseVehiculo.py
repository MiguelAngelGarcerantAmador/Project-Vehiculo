from django.db import models


class ClaseVehiculo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

from django.db import models


class TipoVehiculo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)

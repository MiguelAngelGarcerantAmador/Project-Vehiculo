from django.db import models

from .factura import Factura
from .trazabilidad import Trazabilidad


class Envio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    remitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    trazabilidad_id = models.ForeignKey(Trazabilidad, on_delete=models.CASCADE)

from django.db import models

from .persona import Persona


class OrdenCompra(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    cantidad = models.BigIntegerField()
    descripcion = models.CharField(max_length=254)
    precio_unitario = models.FloatField()
    impuestos = models.FloatField()
    valor_total = models.FloatField()
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)

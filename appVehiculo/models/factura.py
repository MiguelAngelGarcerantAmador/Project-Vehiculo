from django.db import models

from .tipoPago import TipoPago
from .persona import Persona
from .ordenCompra import OrdenCompra


class Factura(models.Model):
    num_factura = models.BigIntegerField(primary_key=True)
    fecha_factura = models.DateTimeField(auto_now=True)
    producto = models.CharField(max_length=255)
    otros_costos = models.FloatField()
    valor_factura = models.FloatField()
    persona_id = models.ForeignKey(Persona, on_delete=models. CASCADE)
    tipo_pago_id = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)

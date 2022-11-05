from django.db import models

from .vehiculo import Vehiculo
from .persona import Persona


class Inventario(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha_lote = models.DateField(auto_now_add=True)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)

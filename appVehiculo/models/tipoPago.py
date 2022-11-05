from django.db import models


class TipoPago(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)

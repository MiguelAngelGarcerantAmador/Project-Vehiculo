from django.db import models


class Persona(models.Model):
    cc = models.BigIntegerField(primary_key=True, serialize=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=8)
    rol = models.CharField(max_length=20)

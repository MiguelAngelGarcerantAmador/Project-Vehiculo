from django.contrib import admin

from appVehiculo.models.claseVehiculo import ClaseVehiculo
from appVehiculo.models.envio import Envio
from appVehiculo.models.factura import Factura
from appVehiculo.models.inventario import Inventario
from appVehiculo.models.ordenCompra import OrdenCompra
from appVehiculo.models.persona import Persona
from appVehiculo.models.tipoPago import TipoPago
from appVehiculo.models.tipoVehiculo import TipoVehiculo
from appVehiculo.models.trazabilidad import Trazabilidad
from appVehiculo.models.vehiculo import Vehiculo

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(TipoVehiculo)
admin.site.register(ClaseVehiculo)
admin.site.register(Inventario)
admin.site.register(Persona)
admin.site.register(OrdenCompra)
admin.site.register(Factura)
admin.site.register(TipoPago)
admin.site.register(Envio)
admin.site.register(Trazabilidad)

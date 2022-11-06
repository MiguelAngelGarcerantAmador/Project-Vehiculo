from django.urls import path

from appVehiculo.views import (
    claseVehiculoView,
    envioView,
    facturaView,
    inventarioView,
    ordenCompraView,
    personaView,
    tipoPagoView,
    tipoVehiculoView,
    trazabilidadView,
    vehiculoView,
)

urlpatterns = [
    path("clase/", claseVehiculoView.gestionClaseVehiculo),
    path("envio/", envioView.gestionEnvio),
    path("factura/", facturaView.gestionFactura),
    path("inventario/", inventarioView.gestionInventario),
    path("ordencompra/", ordenCompraView.gestionOrdenCompra),
    path("persona/", personaView.gestionPersona),
    path("tipopago/", tipoPagoView.gestionTipoPago),
    path("tipovehiculo/", tipoVehiculoView.gestionTipoVehiculo),
    path("trazabilidad/", trazabilidadView.gestionTrazabilidad),
    path("vehiculo/", vehiculoView.gestionVehiculo),
]

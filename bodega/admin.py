from django.contrib import admin

from .models import Producto, Solicitud, DetalleSolicitud

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock']

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['nombre_solicitante', 'direccion_solicitante']

@admin.register(DetalleSolicitud)
class DetalleSolicitudAdmin(admin.ModelAdmin):
    list_display = ['producto', 'solicitud', 'cantidad']
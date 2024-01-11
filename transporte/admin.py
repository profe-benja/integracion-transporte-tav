from django.contrib import admin

# Register your models here.
from .models import SolicitudTransporte

@admin.register(SolicitudTransporte)
class SolicitudTransporteAdmin(admin.ModelAdmin):
    list_display = ('codigo_seguimiento', 'persona_origen', 'direccion_origen', 'persona_destino', 'direccion_destino', 'descripcion', 'estado')
    search_fields = ('codigo_seguimiento', 'persona_origen', 'persona_destino', 'estado')
    list_filter = ('estado',)
    

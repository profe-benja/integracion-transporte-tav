from rest_framework import serializers
from transporte.models import SolicitudTransporte


class SolicitudTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudTransporte  
        fields = '__all__'
        # exclude = ['is_removed', 'created', 'modified']
        # exclude = ['is_removed', 'created', 'modified']
        
        # codigo_seguimiento = models.CharField(max_length=20, unique=True)
        # persona_origen = models.CharField(max_length=100)
        # direccion_origen = models.CharField(max_length=255)
        # persona_destino = models.CharField(max_length=100)
        # direccion_destino = models.CharField(max_length=255)
        # descripcion = models.TextField()
        # estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='pendiente')

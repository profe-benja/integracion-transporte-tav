from django.db import models

# Create your models here.
class SolicitudTransporte(models.Model):
    ESTADOS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )

    codigo_seguimiento = models.CharField(max_length=20, unique=True)
    persona_origen = models.CharField(max_length=100)
    direccion_origen = models.CharField(max_length=255)
    persona_destino = models.CharField(max_length=100)
    direccion_destino = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='pendiente')

    def __str__(self):
        return f"Solicitud {self.codigo_seguimiento} - {self.estado}"
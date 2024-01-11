from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

class Solicitud(models.Model):
    nombre_solicitante = models.CharField(max_length=255)
    direccion_solicitante = models.TextField()

class DetalleSolicitud(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
from rest_framework import serializers
from bodega.models import Producto, Solicitud, DetalleSolicitud

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

class DetalleSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleSolicitud
        fields = '__all__'
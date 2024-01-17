from django.urls import path, include
from .views import data, producto_index, musicpro_index, consumir_api,teclanet

urlpatterns = [
    # path('transporte/', include('transporte.urls')),
    path('producto', producto_index, name="bodega_producto_index"),
    
    path('productos_musicpro', musicpro_index, name="musicpro_index"),
    path('consumir_api', consumir_api, name="consumir_api"),

    path('teclanet', teclanet, name="teclanet_index"),
    
    path('data', data, name="bodega_data")
    
]

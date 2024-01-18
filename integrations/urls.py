from django.urls import path, include
from .views import cargafacil_solicitud, salesforce_productos, teclanet_productos
urlpatterns = [
    path('transporte/cargafacil/solicitud', cargafacil_solicitud, name="cargafacil_solicitud"),
    
    
    path('bodega/salesforce/productos', salesforce_productos, name="salesforce_productos"),
    path('bodega/teclanet/productos', teclanet_productos, name="teclanet_productos"),
    # path('productos_musicpro', musicpro_index, name="musicpro_index"),
    # path('consumir_api', consumir_api, name="consumir_api"),

    # path('teclanet', teclanet, name="teclanet_index"),
    
    # path('data', data, name="bodega_data")
    
]

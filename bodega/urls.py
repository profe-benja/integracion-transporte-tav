from django.urls import path, include
from .views import data, producto_index

urlpatterns = [
    # path('transporte/', include('transporte.urls')),
    path('producto', producto_index, name="bodega_producto_index"),
    path('data', data, name="bodega_data")
    
]

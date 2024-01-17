from django.urls import path
from . import views

urlpatterns = [
    path('productos/',views.lista_productos, name='lista_productos'),
    path('productos/<id>',views.vista_productos, name='vista_productos'),
    
    path('solicitud/',views.lista_solicitud, name='lista_solicitud'),
    
    
    path('saludo/',views.saludo, name='api_saludo'),
    
    
]
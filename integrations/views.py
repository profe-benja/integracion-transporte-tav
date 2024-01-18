from django.shortcuts import render
from .env import *
import requests
# 
# URL_CARGA_FACIL = 'http://192.168.104.138:8000/api/v1/solicitud?format=json'
# Create your views here.
def cargafacil_solicitud(request):
    
    if request.method == 'POST':
        # response = requests.get(url)
        response = requests.post( 
            URL_CARGA_FACIL, 
            data={
                'codigo_seguimiento': "1234556222",
                'persona_origen': "eduardo",
                'direccion_origen': "quinta normal",
                'persona_destino': "jordan",
                'direccion_destino': "nkaka",
                'descripcion': "asdakldald",
                'estado': "entregado"
            })
        
        # response = requests.get(
        #     URL_CARGA_FACIL
        # )
        datos = response.json()
        
        context = {
            'datos': datos
        }
        
        # print(productos)
        print(datos)
    
    return render(request, 'transporte/cargafacil/solicitud.html', context) 



def salesforce_productos(request):
    
    if request.method == 'GET':
        
        response = requests.get(
            URL_SALESFORCE
        )
        datos = response.json()
            
        context = {
            'productos': datos
        }
            
        # print(productos)
        print(datos)
        return render(request, 'bodega/salesforce/productos.html', context) 
    elif request.method == 'POST':
        
        datos = request.POST
        print(datos)
        
        # response = requests.post( 
        #     URL_SALESFORCE, 
        #     data={
        #         'codigo': "1234556222",
        #         'nombre': "eduardo",
        #         'descripcion': "quinta normal",
        #         'precio': "jordan",
        #         'stock': "nkaka",
        #         'estado': "asdakldald"
        #     })
        
        # response = requests.get(
        #     URL_CARGA_FACIL
        # )
        # datos = response.json()
        
        # context = {
        #     'datos': datos
        # }
        
        # print(productos)
        
def teclanet_productos(request):
    
    if request.method == 'GET':
        response = requests.get(
            URL_TECLANET_PRODUCTOS
        )
        datos = response.json()
            
        context = {
            'productos': datos
        }
        return render(request, 'bodega/teclanet/productos.html', context) 
    elif request.method == 'POST':
        print(request.POST)
        
        productos = request.POST['productos']
        
        for id,p in enumerate(productos):
            print(f" PRODUCTO {id}   -> {p}")
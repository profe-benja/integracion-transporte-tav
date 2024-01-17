from django.shortcuts import render
from .models import Producto, Solicitud, DetalleSolicitud
from faker import Faker
import requests

fake = Faker()


def teclanet(request):
    api_url = "http://192.168.211.120:8000/api/sistema_bodega/v1/productos/"

    # Realizar la solicitud GET a la API
    response = requests.get(api_url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        productos = response.json()

        # Renderizar la plantilla con la lista de productos
        return render(request, 'teclanet/index.html', {'productos': productos})
    else:
        # Manejar el error en caso de que la solicitud no sea exitosa
        return render(request, 'miapp/error.html', {'error_message': 'Error al obtener la lista de productos'})


def musicpro_index(request):
    url = 'https://musicpro.bemtorres.win/api/v1/bodega/producto'
    response = requests.get(url)
    productos = response.json()
    
    context = {
        'productos': productos['productos']
    }
    
    # print(productos)
    return render(request, 'bodega/musicpro/index.html', context)

def consumir_api(request):
    url = 'https://musicpro.bemtorres.win/api/v1/test/parametro/1'
    # response = requests.get(url)
    response = requests.post(url, data={'nombre': 'Juan', 'apellido': 'Perez', 'edad': 200})
    # response = requests.put(url, data={'nombre': 'Juan'})
    
    datos = response.json()
    
    context = {
        'datos': datos
    }
    
    # print(productos)
    return render(request, 'bodega/musicpro/vacio.html', context)


def producto_index(request):
    productos = Producto.objects.all()
    return render(request, 'bodega/producto_index.html', {'productos': productos})

# Create your views here.
def data(request):
    for _ in range(100):
        Producto.objects.create(
            nombre=fake.word(),
            descripcion=fake.text(),
            precio=fake.random_int(min=1, max=100),
            stock=fake.random_int(min=1, max=100)
        )

    # Generar datos ficticios para solicitudes y detalles
    for _ in range(20):
        solicitud = Solicitud.objects.create(
            nombre_solicitante=fake.name(),
            direccion_solicitante=fake.address()
        )

        for _ in range(5):
            producto = Producto.objects.order_by('?').first()
            DetalleSolicitud.objects.create(
                producto=producto,
                solicitud=solicitud,
                cantidad=fake.random_int(min=1, max=10)
            )

    return True
    # return render(request, 'bodega/data.html', {})
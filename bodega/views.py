from django.shortcuts import render
from .models import Producto, Solicitud, DetalleSolicitud
from faker import Faker

fake = Faker()

def producto_index(request):
    productos = Producto.objects.all()
    return render(request, 'bodega/producto_index.html', {'productos': productos})

# Create your views here.
def data(request):
    for _ in range(10):
        Producto.objects.create(
            nombre=fake.word(),
            descripcion=fake.text(),
            precio=fake.random_int(min=1, max=100),
            stock=fake.random_int(min=1, max=100)
        )

    # Generar datos ficticios para solicitudes y detalles
    for _ in range(5):
        solicitud = Solicitud.objects.create(
            nombre_solicitante=fake.name(),
            direccion_solicitante=fake.address()
        )

        for _ in range(3):
            producto = Producto.objects.order_by('?').first()
            DetalleSolicitud.objects.create(
                producto=producto,
                solicitud=solicitud,
                cantidad=fake.random_int(min=1, max=10)
            )

    return True
    # return render(request, 'bodega/data.html', {})
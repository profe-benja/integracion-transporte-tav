from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.parsers import JSONParser


from bodega.models import Producto, Solicitud, DetalleSolicitud

from .serializers import ProductoSerializer

@csrf_exempt # para que no pida token
@api_view(['GET', 'POST']) # solo acepta peticiones GET y POST
def lista_productos(request):
    # 1 mostrar todos los productos
    # 2 crear un producto
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt # para que no pida token
@api_view(['GET', 'PUT', 'DELETE'])     
def vista_productos(request, id):
    # 2 mostrar un producto en particular
    if request.method == 'GET':
        try:
            producto = Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        try:
            producto = Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = JSONParser().parse(request)
        # actualiza el producto
        serializer = ProductoSerializer(producto, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            producto = Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# POST api/bodega/v1/solicitud 
@csrf_exempt # para que no pida token
@api_view(['POST'])   
def lista_solicitud(request):
    print(request.data)
    
    nombre = request.data['nombre']
    direccion = request.data['direccion']
    productos = request.data['productos']
    
    solicitud = Solicitud.objects.create(
        nombre_solicitante=nombre,
        direccion_solicitante=direccion
    )

    print("\n\n\n")
    for p in productos:
        
        producto_id = p['id_producto']
        cantidad = p['cantidad']

        producto = Producto.objects.get(pk=producto_id)

        DetalleSolicitud.objects.create(
            producto=producto,
            solicitud=solicitud,
            cantidad=cantidad
        )
        print(f"producto {p['id_producto']} cantidad {p['cantidad']}")
    print("\n\n\n")
    
    
    # creacion de un solicitud
    
    # Solicitud.objects.create(nombre=nombre, direccion=direccion)
    # So
    
    # print(f"estos son todos los productos {productos}")
    
    return Response(request.data)

@csrf_exempt # para que no pida token
@api_view(['GET', 'POST'])   
def saludo(request):
    
    if request.method == 'POST':
        respond = {
            'mensaje2':'¿como estai?',
            'recibido': request.data
        }
        
        return Response(respond)
    
    return Response({'mensaje':'hola mundo'})
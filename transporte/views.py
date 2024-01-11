from django.shortcuts import render
from .models import SolicitudTransporte

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        # buscar el codigo de seguimiento
        codigo_seguimiento = request.POST.get('codigo_seguimiento', '')
        # Realiza la búsqueda en la base de datos
        resultados = SolicitudTransporte.objects.filter(codigo_seguimiento=codigo_seguimiento).first()
        
        print(resultados)
        print(codigo_seguimiento)
        
        return render(request, 'index.html', {'resultados': resultados, 'codigo_seguimiento': codigo_seguimiento})
    
    
    return render(request, 'index.html')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Estado, Municipio

def selector_view(request):
    """
    Renderiza la página principal con el selector de estados.
    """
    estados = Estado.objects.all()
    context = {
        'estados': estados
    }
    return render(request, 'geografia/selector.html', context)

def cargar_municipios_view(request):
    """
    Vista que maneja la petición AJAX para obtener los municipios.
    """
    estado_id = request.GET.get('estado_id')
    
    municipios = Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
    
    data = [{'id': municipio.id, 'nombre': municipio.nombre} for municipio in municipios]
    
    return JsonResponse(data, safe=False)
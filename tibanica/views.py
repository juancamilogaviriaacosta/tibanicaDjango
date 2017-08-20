from django.shortcuts import render
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def socioecologico(request):
    return render(request, 'socioecologico.html')

def biodiversidad(request):
    return render(request, 'biodiversidad.html')

def cartografia(request):
    return render(request, 'cartografia.html')

def biblioteca(request):
    return render(request, 'biblioteca.html')

def comic(request):
    return render(request, 'comic.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def paginasamigas(request):
    return render(request, 'paginasamigas.html')

def visitahumedal(request):
    context = {
        'apikey': os.environ.get('apikey')
    }
    return render(request, 'visitahumedal.html', context)


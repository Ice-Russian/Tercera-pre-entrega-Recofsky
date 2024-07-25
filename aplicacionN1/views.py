from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "aplicacionN1/index.html")
def curso(request):
    return render(request, "aplicacionN1/cursos.html")
def estudiantes(request):
    return render(request, "aplicacionN1/estudiantes.html")
def profesores(request):
    return render(request, "aplicacionN1/profesores.html")
def entregables(request):
    return render(request, "aplicacionN1/entregables.html")

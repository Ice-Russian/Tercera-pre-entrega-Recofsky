from django.shortcuts import render
from django.http import HttpResponse
from aplicacionN1.models import Curso
from config.forms import CursoFormulario, BuscaCursoForm
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

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()

            return render(request, "aplicacionN1/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "aplicacionN1/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "aplicacionN1/mostrar_cursos.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "aplicacionN1/buscar_form_con_api.html", {"miFormulario": miFormulario})
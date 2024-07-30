from django.shortcuts import render
from django.http import HttpResponse
from aplicacionN1.models import Curso, Estudiante, Profesor, Entregable
from config.forms import CursoFormulario, BuscaCursoForm, EstudianteFormulario, BuscarEstudianteForm, ProfesorFormulario, BuscarProfesorForm, EntregableFormulario

# Paginas de Inicio

def inicio(request):
    return render(request, "aplicacionN1/index.html")
def curso(request):
    return render(request, "aplicacionN1/cursos.html")
def estudiantes(request):
    return render(request, "aplicacionN1/estudiantes.html")
def profesores(request):
    return render(request, "aplicacionN1/profesores.html")
def entregables(request):
    return render(request, "aplicacionN1/entregrable.html")

# Fin de paginas de inicio

# Formularios // Agregar

def agregar_curso(request):
    if request.method == "POST":
        formaddCurso = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if formaddCurso.is_valid():
            informacion = formaddCurso.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()

            return render(request, "aplicacionN1/AccionExitosa.html")
    else:
        formaddCurso = CursoFormulario()

    return render(request, "aplicacionN1/cursos_form_add.html", {"formaddCurso": formaddCurso})

def agregar_estudiante(request):
    if request.method == "POST":
        formaddEstudiante = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if formaddEstudiante.is_valid():
            informacion = formaddEstudiante.cleaned_data
            
            estudiantes = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiantes.save()

            return render(request, "aplicacionN1/estudiantes.html")
    else:
        formaddEstudiante = EstudianteFormulario()

    return render(request, "aplicacionN1/estudiantes_form_add.html", {"formaddEstudiante": formaddEstudiante})

def agregar_profesor(request):
    if request.method == "POST":
        formaddProfesores = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if formaddProfesores.is_valid():
            informacion = formaddProfesores.cleaned_data
            
            profesores = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion['profesion'])
            profesores.save()

            return render(request, "aplicacionN1/AccionExitosa.html")
    else:
        formaddProfesores = ProfesorFormulario()

    return render(request, "aplicacionN1/Profesores.html", {"formaddProfesores": formaddProfesores})

# Fin Agregar

# Formulario // Busquedas 

def buscar_curso(request):
    if request.method == "POST":
        formsearchCurso = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if formsearchCurso.is_valid():
            informacion = formsearchCurso.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["nombre"])

            return render(request, "aplicacionN1/cursos_print.html", {"cursos": cursos})
    else:
        formsearchCurso = BuscaCursoForm()

    return render(request, "aplicacionN1/cursos_form_search.html", {"formsearchCurso": formsearchCurso})

def buscar_estudiante(request):
    if request.method == "POST":
        formsearchEstudiante = BuscarEstudianteForm(request.POST)

        if formsearchEstudiante.is_valid():
            informacion = formsearchEstudiante.cleaned_data
            
            estudiantes = Estudiante.objects.filter(nombre__icontains=informacion["nombre"])
            return render(request, "aplicacionN1/estudiantes_print.html", {"estudiante": estudiantes})
    else:
        formsearchEstudiante = BuscarEstudianteForm()

    return render(request, "aplicacionN1/estudiantes_form_search.html", {"formsearchEstudiante": formsearchEstudiante})

# Fin Busqueda

# Entregable

def entrega(request):
    if request.method == "POST":
        formEntregables = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if formEntregables.is_valid():
            informacion = formEntregables.cleaned_data
            
            entregable = Entregable(nombre=informacion["nombre"], fecha_de_entrega__date=informacion["fecha_de_entrega"], entregado=informacion["entregado"])
            entregable.save()

            return render(request, "aplicacionN1/index.html")
    else:
        formEntregables = EntregableFormulario()

    return render(request, "aplicacionN1/entregables.html", {"formEntregables": formEntregables})

# Fin entregable
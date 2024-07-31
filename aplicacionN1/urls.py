from django.urls import path
from aplicacionN1.views import *

urlpatterns = [
    path('', inicio, name='index'),

    path('cursos/', curso, name='cursos'),
    path('agregarcursos/', agregar_curso, name="agregarcursos"),
    path('buscarcursos/', buscar_curso, name="buscarcursos"),

    path('estudiantes/', estudiantes, name='estudiantes'),
    path('agregarestudiantes/', agregar_estudiante, name='agregarestudiantes'),
    path('buscarestudiantes/', buscar_estudiante, name='buscarestudiantes'),

    path('profesores/', profesores, name='profesores'),
    path('agregarprofesores/', agregar_profesor, name='agregarprofesor'),
    path('buscarprofesores/', buscar_profesor, name='buscarprofesor'),

    path('entregables/', entrega, name='entregables'),

]

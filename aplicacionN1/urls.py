from django.urls import path
from aplicacionN1.views import *

urlpatterns = [
    path('', inicio, name='index'),
    path('cursos/', curso, name='cursos'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', agregar_profesor, name='profesores'),
    path('entregables/', entrega, name='entregables'),
    path('agregarcursos/', agregar_curso, name="agregarcursos"),
    path('buscarcursos/', buscar_curso, name="buscarcursos"),
    path('agregarestudiantes/', agregar_estudiante, name='agregarestudiantes'),
    path('buscarestudiantes/', buscar_estudiante, name='buscarestudiantes'),

]

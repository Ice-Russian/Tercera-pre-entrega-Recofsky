from django.urls import path
from aplicacionN1.views import *

urlpatterns = [
    path('', inicio, name='index'),
    path('cursos/', curso, name='cursos'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name='profesores'),
    path('entregables/', entregables, name='entregables'),
    path('curso-formulario/', form_con_api, name="CursoFormulario"),
    path('buscar-form-con-api/', buscar_form_con_api, name="Buscar_Form_Con_Api"),
]

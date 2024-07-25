from django.urls import path
from aplicacionN1.views import *

urlpatterns = [
    path('', inicio, name='index'),
    path('cursos/', curso, name='cursos'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name='profesores'),
    path('entregables/', entregables, name='entregables'),
]

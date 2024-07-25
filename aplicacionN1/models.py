from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision =models.IntegerField()
    def __str__(self):
        return f"Nombre del curso:{self.nombre} || Comision: {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre del Estudiante:{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre del Profesor:{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
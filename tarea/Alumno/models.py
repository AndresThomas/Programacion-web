from django.db import models

# Create your models here.
class Materia(models.Model):
    nombreMateria = models.CharField(max_length=100, null=False)


class Alumno(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    carrera = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    matricula = models.IntegerField(null=False)
    materiaAlumno = models.ForeignKey(Materia, on_delete=models.CASCADE)
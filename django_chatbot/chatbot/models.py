from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    codigo = models.IntegerField(primary_key=True, null=False)
    primerParcial = models.CharField(max_length=22, null=False, default='Nota no disponible')
    segundoParcial = models.CharField(max_length=22, null=False, default='Nota no disponible')
    TercerParcial = models.CharField(max_length=22, null=False, default='Nota no disponible')
    faltas = models.IntegerField(null=False, default=0)

class Tarea(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    descripcion = models.CharField(max_length=255, default='Tarea de clases')
    nota = models.IntegerField(default=-1, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    entregado = models.BooleanField(null=False, default=False)
    fecha = models.DateField(null=False)

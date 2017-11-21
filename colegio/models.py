from django.db import models
from django.utils import timezone
from django.contrib import admin

class Alumno(models.Model):
    carnet=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return '{}'.format(self.nombre)

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    profesion=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Materia(models.Model):
    nombre=models.CharField(max_length=50)
    creditos= models.IntegerField()
    alumno = models.ManyToManyField(Alumno, through='Nota')
    profesor = models.ForeignKey(Profesor,null=True )
    def __str__(self):
        return '{}'.format(self.nombre)

class Nota (models.Model):
    material = models.ForeignKey(Materia, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.CharField(max_length=50, blank=True)

class NotaInLine(admin.TabularInline):
    model = Nota
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (NotaInLine,)

class AlumnoAdmin (admin.ModelAdmin):
    inlines = (NotaInLine,)

class Grado(models.Model):
    """docstring forGrado."""
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=10)
    materia = models.ManyToManyField(Materia, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

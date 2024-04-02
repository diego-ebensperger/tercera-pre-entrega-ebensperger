from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cursos = models.ManyToManyField(Curso, related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



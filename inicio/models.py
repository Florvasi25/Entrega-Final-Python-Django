from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=20) 
    edad = models.IntegerField()
    email = models.CharField(max_length=50) 
    numero_telefono = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'Nombre: {self.nombre} --- E-mail: {self.email}'

class Productos(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
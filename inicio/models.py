from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=20) 
    edad = models.IntegerField()
    email = models.CharField(max_length=50) 
    numero_telefono = models.IntegerField()
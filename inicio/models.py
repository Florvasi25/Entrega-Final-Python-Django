from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=20) 
    edad = models.IntegerField()
    email = models.CharField(max_length=50) 
    numero_telefono = models.IntegerField()
    descripcion = RichTextField(null=True, blank=True)


    def __str__(self):
        return f'Nombre: {self.nombre} --- E-mail: {self.email}'


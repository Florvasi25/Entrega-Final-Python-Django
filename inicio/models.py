from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=20) 
    modelo = models.CharField(max_length=20, null=True, blank=True) 
    precio = models.IntegerField()
    numero_telefono = models.IntegerField()
    descripcion = RichTextField(null=True, blank=True)
    email_vendedor = models.EmailField()
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    fecha_creacion = models.DateField()
    usuario_vendedor = models.CharField(max_length=20)
    


    def __str__(self):
        return f'Nombre: {self.nombre}'


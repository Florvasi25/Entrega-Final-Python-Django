from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Mensaje(models.Model):
    texto = RichTextField(null=True, blank=True)
    autor = models.CharField(max_length=30)
    destinatario = models.CharField(max_length=30)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f'Autor: {self.autor}'


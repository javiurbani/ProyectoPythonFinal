from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


# Create your models here.

class Articulo(models.Model):

    def __str__(self):
        return f"Artículo: {self.nombre} - {self.animal}"

    nombre = models.CharField(max_length=60)
    animal = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField() 
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="images")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)



class Review(models.Model):

    comentario = models.CharField(max_length=120)
    usuario = models.CharField(max_length=30)


class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)

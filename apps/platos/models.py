from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre_plato=models.CharField(max_length=40)
    precio=models.IntegerField(max_length=6)
    procedencia= models.CharField(max_length=40)

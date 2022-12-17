from django.db import models

class Clientes(models.Model):
    nombre_cliente=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni = models.IntegerField(max_length=10)

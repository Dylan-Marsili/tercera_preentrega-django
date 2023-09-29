from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    cargo = models.CharField(max_length=30)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


class Cita(models.Model):
    nombrep = models.CharField(max_length=30)
    fecha = models.DateField()
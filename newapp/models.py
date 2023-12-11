from django.db import models

#Cree la clase Member(Miembro), ese nombre lo designe para los trabajadores.

class Member(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)

from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.telefono})"

class Top(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField()

class Camisas(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField() 

class Pantalones(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField()
    
    def __str__(self):
        return f"{self.talle} {self.marca}"

class Short(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField()

class Camperas(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField()
def __str__(self):
        return f"{self.talle} {self.marca}"

class Championes(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField()


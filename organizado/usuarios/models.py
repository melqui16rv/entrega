from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    documento=models.IntegerField()
    ficha=models.IntegerField()
    photo=models.ImageField(upload_to='fotos_usurios')

    def __str__(self):
        return self.nombre


    
class Image(models.Model):
    photo=models.ImageField(upload_to='fotos') 
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    telefono=models.IntegerField()

    def __str__(self):
        return self.photo
    # ,self.nombre, self.apellido, self.email,self.telefono
    
class Actualizar(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    telefono=models.IntegerField()



class FormularioAgenda(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.fecha} - {self.hora}: {self.descripcion}'
    
class Agenda(models.Model):
    # Definir los campos de la Agenda aquí
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Agenda {self.id}"
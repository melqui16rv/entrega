from django.db import models

class HojaVida(models.Model):
    nombre = models.CharField(max_length=255)
    documento = models.CharField(max_length=20)
    libreta_militar = models.BooleanField()
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    habilidades = models.TextField()  
    estudios = models.TextField()     
    curriculum = models.FileField(upload_to='curriculums/')

    def __str__(self):
        return self.nombre

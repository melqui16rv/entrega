from django.db import models

class HojaVida(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    educacion = models.TextField()
    Certificado = models.FileField(upload_to='educacion_pdfs/')
    experiencia = models.TextField()
    profesion = models.CharField(max_length=100)
    curriculum = models.FileField(upload_to='curriculums/')

    def __str__(self):
        return self.nombre

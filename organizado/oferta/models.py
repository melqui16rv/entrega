from django.db import models

# Create your models here.
class Oferta(models.Model):
    codigo = models.IntegerField()
    profecion = models.CharField(max_length=255)
    experiencia = models.CharField(max_length=255)
    educacion = models.CharField(max_length=255)
    sueldo = models.FloatField()
    tipo_contrato = models.CharField(max_length=255)
    modalidad_trabajo = models.CharField(max_length=255)
    localizacion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    n_vacantes = models.IntegerField()
    postulaciones = models.IntegerField()

    def __str__(self):
        return self.profecion
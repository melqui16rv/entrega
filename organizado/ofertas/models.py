from django.db import models

class Oferta(models.Model):
    codigo = models.IntegerField()
    profecion = models.CharField(max_length=255, null=True)
    experiencia = models.CharField(max_length=255)
    educacion = models.CharField(max_length=255)
    sueldo = models.FloatField()
    tipo_contrato = models.CharField(max_length=255)
    modalidad_trabajo = models.CharField(max_length=255)
    localizacion = models.CharField(max_length=255)
    n_vacantes = models.IntegerField()
    postulaciones = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f'{self.codigo} - {self.profecion}'

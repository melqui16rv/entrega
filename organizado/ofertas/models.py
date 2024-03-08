from django.db import models

# Create your models here.
class Oferta(models.Model):
    codigo = models.IntegerField()
    nombre_cargo = models.CharField(max_length=255)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    experiencia = models.TextField()
    tipo_contrato = models.CharField(max_length=255)
    modalidad_trabajo = models.CharField(max_length=255)
    localizacion = models.CharField(max_length=255)
    n_vacantes = models.IntegerField()
    postulaciones = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f'{self.codigo} - {self.nombre_cargo}'
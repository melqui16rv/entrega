from django.db import models
# Create your models here.
from django.db import models

class Agenda(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Agenda - {self.fecha} {self.hora}"
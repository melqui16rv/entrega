import bcrypt
from django.db import models

class regis_candidato(models.Model):
    nombre = models.CharField(max_length=50)
    documento = models.IntegerField()
    correo = models.EmailField(max_length=254)
    contraseña_hashed = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.nombre

    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.contraseña_hashed = hashed_password.decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.contraseña_hashed.encode('utf-8'))

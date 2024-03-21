from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

class ImageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image'

class FormularioAgenda(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agenda'

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Usuario
from . models import Ofertas
from . models import Image
from .models import FormularioAgenda
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Ofertas)
admin.site.register(Image)
# class FormularioAgendaAdmin(admin.ModelAdmin):
#     list_display = ['fecha', 'hora', 'descripcion']

# admin.site.register(FormularioAgenda, FormularioAgendaAdmin)
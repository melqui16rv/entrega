from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import regis_candidato

class Inicio_sesion(forms.ModelForm):
    class Meta: 
        model = regis_candidato
        fields = ['correo','contraseña_hashed']


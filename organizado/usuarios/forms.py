from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Image
from .models import FormularioAgenda
from .models import Agenda


class ImageForm(forms.ModelForm):
    class meta:
        model = Image
        fields = ("photo",
                   "nombre",
                   "apelledio",
                   "email",
                   "telefono"
                   )





# class FormularioAgendaForm(forms.ModelForm):
#     class Meta:
#         model = FormularioAgenda
#         fields = ['fecha', 'hora', 'descripcion']

# class AgendaForm(forms.ModelForm):
#     class Meta:
#         model = Agenda
#         fields = ['fecha', 'hora', 'descripcion']
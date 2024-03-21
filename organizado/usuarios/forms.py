from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Image



class ImageForm(forms.ModelForm):
    class meta:
        model = Image
        fields = ("photo",
                   "nombre",
                   "apelledio",
                   "email",
                   "telefono"
                   )

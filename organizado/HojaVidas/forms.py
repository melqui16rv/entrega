# En HojaVidas/forms.py
from django import forms
from .models import HojaVida

class HojaVidaForm(forms.ModelForm):
    class Meta:
        model = HojaVida
        fields = '__all__'

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Oferta

from django import forms
from .models import Oferta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class OfertaForm(forms.ModelForm):
    EDUCACION_CHOICES = [
        ('Primaria', 'Primaria'),
        ('Secundaria', 'Secundaria'),
        ('Bachillerato', 'Bachillerato'),
        ('Técnico', 'Técnico / Formación Profesional'),
        ('Universidad', 'Universidad'),
        ('Maestría', 'Maestría'),
        ('Postgrado', 'Postgrado')
    ]

    educacion = forms.ChoiceField(label='Educación', choices=EDUCACION_CHOICES, required=False)

    class Meta:
        model = Oferta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OfertaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'codigo',
            'profecion',
            'experiencia',
            'educacion',
            'sueldo',
            'tipo_contrato',
            'modalidad_trabajo',
            'localizacion',
            'n_vacantes',
            'postulaciones',
            'fecha_inicio',
            'fecha_fin',
            Submit('submit', 'Guardar')
        )



class Actualizacion(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__'

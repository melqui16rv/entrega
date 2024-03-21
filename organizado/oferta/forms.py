from agendas import forms
from oferta.models import Oferta
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class OfertaForm(forms.ModelForm):
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
            'fecha_inicio',
            'fecha_fin',
            'n_vacantes',
            'postulaciones',
            Submit('submit', 'Guardar')

        )


class Actualizacion(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__'

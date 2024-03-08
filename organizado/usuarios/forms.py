from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Ofertas  # Asegúrate de importar tu modelo
from .models import Image
from .models import FormularioAgenda
from .models import Agenda
class OfertaForm(forms.ModelForm):
    class Meta:
        model = Ofertas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OfertaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'codigo',
            'nombre_cargo',
            'sueldo',
            'experiencia',
            'tipo_contrato',
            'modalidad_trabajo',
            'localizacion',
            'n_vacantes',
            'postulaciones',
            'fecha_inicio',
            'fecha_fin',
            Submit('submit', 'Guardar')

        )

class ImageForm(forms.ModelForm):
    class meta:
        model = Image
        fields = ("photo",
                   "nombre",
                   "apelledio",
                   "email",
                   "telefono"
                   )

class Actualizacion(forms.ModelForm):
    class Meta:
        model = Ofertas
        fields = '__all__'




# class FormularioAgendaForm(forms.ModelForm):
#     class Meta:
#         model = FormularioAgenda
#         fields = ['fecha', 'hora', 'descripcion']

# class AgendaForm(forms.ModelForm):
#     class Meta:
#         model = Agenda
#         fields = ['fecha', 'hora', 'descripcion']
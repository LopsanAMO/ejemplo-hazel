from django import forms
from proyecto.models import Estudiante

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class LogForm(forms.Form):
    username = forms.CharField(label='Usurario')
    boleta = forms.CharField(label='Boleta')

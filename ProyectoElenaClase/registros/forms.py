from django import forms
from .models import ComentariosContacto, Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentariosContactoForm(forms.ModelForm):
    class Meta:
        model = ComentariosContacto
        fields = ['usuario', 'mensaje']

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ('titulo', 'descripcion', 'archivo')
        widgets = {
            'archivo': CustomClearableFileInput
        }


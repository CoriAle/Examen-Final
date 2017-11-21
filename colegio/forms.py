from django import forms
from .models import Grado, Materia

class GradoForm(forms.ModelForm):
    """docstring fo PostForm."""
    class Meta:
        model = Grado
        fields = ('nombre', 'seccion','materia',)

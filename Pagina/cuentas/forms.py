from django import forms
from django.contrib.auth.models import User
from .models import Perfil

# Formulario para editar el perfil del usuario
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'fecha_nacimiento']

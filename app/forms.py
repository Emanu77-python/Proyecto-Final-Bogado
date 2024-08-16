from django import forms
from .models import Publicacion
from django.contrib.auth.models import User
from django.contrib.auth.forms import  AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']  
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ej: La mejor jugada de mi vida...',
                'class': 'form-control'
            }),
            'subtitulo': forms.TextInput(attrs={
                'placeholder': 'Ej: Un giro inesperado...',
                'class': 'form-control'
            }),
            'contenido': forms.Textarea(attrs={
                'placeholder': 'Describe tu experiencia, por ejemplo: Gané en tiempo récord con una jugada épica...',
                'class': 'form-control',
                'rows': 5
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }
from django import forms
from django.forms.widgets import Textarea


class ContactoForm(forms.Form):
    nombre=forms.CharField(label="Nombre",max_length=35, required=True)
    
    email=forms.CharField(label="Email",max_length=35, required=True)

    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)

    

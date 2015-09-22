from django import forms

from .models import Carga

class FormCarga(forms.ModelForm):

    class Meta:
        model = Carga
        fields = ('valor','dados','usuario',)
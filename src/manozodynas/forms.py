from django import forms
from .models import Terminai


class TerminoForma(forms.ModelForm):
    class Meta:
        model = Terminai

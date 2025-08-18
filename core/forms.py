from django import forms
from .models import Sala, Reserva
from django.utils.timezone import now
from django.forms.widgets import DateInput


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['sala', 'data', 'hora_inicio', 'hora_fim']
        widgets = {
            'data': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

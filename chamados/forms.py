from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Chamado, Setor
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'descricao', 'setor', 'data','hora_chamado', 'usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 5}),
            'hora_chamado': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'hora_chamado': 'Horario',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.data:
            self.initial['data'] = self.instance.data.strftime('%Y-%m-%d')
class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome']

class AtualizarChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['atendido', 'data_atendimento', 'hora_atendimento', 'tecnico']
        widgets = {
            'data_atendimento': forms.DateInput(format = settings.DATETIME_FORMAT, attrs={'type': 'date'}),
            'hora_atendimento': forms.TimeInput(attrs={'type': 'time'}),
        }
class Chamado_Editar_Form(forms.Form):
    class Meta:
        model = Chamado
        fields = ['titulo', 'descricao', 'setor', 'data', 'usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }
    
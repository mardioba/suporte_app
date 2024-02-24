from django import forms
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
        fields = ['titulo', 'descricao', 'setor', 'data', 'usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }
class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome']

class AtualizarChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['atendido', 'data_atendimento', 'tecnico']
        widgets = {
            'data_atendimento': forms.DateInput(attrs={'type': 'date'}),
        }

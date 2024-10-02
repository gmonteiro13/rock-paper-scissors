from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Jogo

class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            "placeholder": "Digite seu nome de usuário"
        }
    ))
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            "placeholder": "Digite a senha"
        })
    )

class CriarContaForm(UserCreationForm):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            "placeholder": "Digite seu nome de usuário"
        })
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            "placeholder": "Mín. 8 caracteres"
        })
    )
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirme a senha"
        })
    )

class JogoForm(forms.Form):
    opcao_usuario = forms.ChoiceField(
        label='Escolha uma opção',
        choices=Jogo.ESCOLHAS_JOGO
    )
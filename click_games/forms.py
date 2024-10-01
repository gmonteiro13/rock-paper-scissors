from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Jogo

class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuário',
        widget=forms.TextInput()
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput()
    )

class CriarContaForm(UserCreationForm):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput()
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput()
    )

class JogoForm(forms.Form):
    opcao_usuario = forms.ChoiceField(
        label='Escolha uma opção',
        choices=Jogo.ESCOLHAS_JOGO
    )
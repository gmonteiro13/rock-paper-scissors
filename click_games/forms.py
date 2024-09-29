from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuário',
        widget=forms.TextInput()
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput()
    )
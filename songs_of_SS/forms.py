from .models import *
from django import forms


from django.forms import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Логін'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        # widgets = {
        #     'username' : TextInput(attrs={'placeholder':'Логін'}),
        #     'password1' : PasswordInput(attrs={'placeholder':'Пароль'}),
        #     'password2' : PasswordInput(attrs={'placeholder':'Повтор пароля'}),
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Логін'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))

    # class Meta:
    #     model = User
    #     fields = ('user', 'password')

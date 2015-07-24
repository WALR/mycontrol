# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30,
                            widget= forms.TextInput(attrs={
                                'class' : 'form-control',
                                'placeholder' : 'Ingrese su Usuario',
                                'required' : 'True'
                            }))
    password = forms.CharField(max_length=30,
                            widget = forms.PasswordInput(attrs={
                                'class' : 'form-control',
                                'placeholder' : 'Ingrese su Contraseña',
                                'required' : 'True'
                            }))

# class RFPAuthForm(AuthenticationForm):
#     username = forms.CharField(widget=TextInput(attrs={'class': 'span2','placeholder': 'Email'}))
#     password = forms.CharField(widget=PasswordInput(attrs={'class': 'span2','placeholder':'Password'}))
    # def clean(self):
    #     if self.cleaned_data.get('username') and self.cleaned_data.get('password'):
    #         username = self.cleaned_data.get('username')
    #         username_exist = User.objects.filter(username = username).exists()

    #     if username_exist:
    #         user = User.objects.get(username = username)

    #     if not user.check_password(self.cleaned_data.get("password")):
    #         self.add_error('password', 'La contraseña es incorrecta')

    #     else:
    #         self.add_error('username', 'El usuario no existe!')

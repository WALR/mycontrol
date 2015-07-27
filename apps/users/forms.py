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

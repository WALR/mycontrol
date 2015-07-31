# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import User

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


class UserPassForm(forms.ModelForm):
    
    class Meta:
        model = User
        #exclude = ('email',)
        
        widgets = {
            'email' : forms.TextInput(attrs={'class' : 'form-control', 'readonly':'readonly'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
            'avatar' : forms.FileInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }
        



# class ProductoForm(forms.ModelForm):
# class Meta:
# model = Producto
# exclude = ('slug',)
# widgets = {
# 'barcode' : forms.NumberInput(attrs={'class' : 'form-control'}),
# 'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
# 'descripcion' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : '2'}),
# 'marca' : forms.Select(attrs={'class' : 'form-control'}),
# 'existencia' : forms.NumberInput(attrs={'class' : 'form-control'}),
# 'precioVenta' : forms.NumberInput(attrs={'class' : 'form-control'}),
# 'precioCompra' : forms.NumberInput(attrs={'class' : 'form-control'}),
# 'precioPorMayor' : forms.NumberInput(attrs={'class' : 'form-control'}),
# 'imagen' : forms.FileInput(attrs={'class' : 'form-control'}),
# 'sucursal' : forms.Select(attrs={'class' : 'form-control'}),
# 'proveedor' : forms.Select(attrs={'class' : 'form-control'}),
# 'categoria' : forms.Select(attrs={'class' : 'form-control'}),
# 'user' : forms.Select(attrs={'class' : 'form-control'})
# }
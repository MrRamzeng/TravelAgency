# -*- coding: utf-8 -*- #
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.admin.widgets import AdminDateWidget

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(min_length=8, max_length=50, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class EditForm(forms.ModelForm):
    last_name = forms.CharField(required=True, max_length=30)
    first_name = forms.CharField(required=True, max_length=30)
    patronymic = forms.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+7\s[(]{1}[0-9]{3}[)]{1}\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')
    phone = forms.CharField(validators=[phone_regex], max_length=20)
    #birthday = forms.DateField(widget=AdminDateWidget)
    email = forms.EmailField(required=True, max_length=254)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'phone', 'email')
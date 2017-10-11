# -*- coding: utf-8 -*- #
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(max_length=30, help_text='Фамилия')
    first_name = forms.CharField(max_length=30, help_text='Имя')
    patronymic = forms.CharField(max_length=30, help_text='Отчество')
    email = forms.EmailField(max_length=254, help_text='Введите корректный Е-mail.')

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'patronymic', 'email', 'password1', 'password2', )
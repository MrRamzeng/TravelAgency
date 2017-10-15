# -*- coding: utf-8 -*- #
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Имя', label=_(u'Имя'))
    last_name = forms.CharField(max_length=30, help_text='Фамилия', label=_(u'Фамилия'))
    email = forms.EmailField(max_length=254, help_text='Введите корректный Е-mail адрес.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

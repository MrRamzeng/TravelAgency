# -*- coding: utf-8 -*- #
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):
    last_name = forms.CharField(max_length=30, label=_(u'Фамилия'))
    first_name = forms.CharField(max_length=30, label=_(u'Имя'))
    phone = forms.CharField(max_length=20, label=_(u'Номер телефона'))
    email = forms.EmailField(max_length=254, help_text='Введите корректный Е-mail адрес.')

class Meta:
    model = User
    fields = ('username', 'last_name', 'first_name', 'phone', 'email', 'password1', 'password2', )

# -*- coding: utf-8 -*- #
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):
    last_name = forms.CharField(
        max_length=30, 
        help_text="Обязательно поле.", 
        label=_(u'Фамилия'))
    first_name = forms.CharField(
        max_length=30,
         help_text="Обязательное поле.",
          label=_(u'Имя'))
    email = forms.EmailField(
        max_length=254,
        help_text='Обязательное поле!')

    class Meta:
        model = User
        fields = (
            'username',
            'last_name',
            'first_name', 
            'email', 
            'password1', 
            'password2')
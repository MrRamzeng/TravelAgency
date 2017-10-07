# -*- coding: utf-8 -*- #
from django.shortcuts import render, redirect

from . models import Manager, Tourist, Country, City, Tour, Region

from itertools import groupby

from collections import OrderedDict

from datetime import datetime, timedelta, date

from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm

def index(request):
    
    return render(request, "Travel/index.html")

def regions(request):
    region = Region.objects.all()
    return render(request, "Travel/regions.html", {'region': region})

def region_city(request, region_id = None):
    region = Region.objects.get(id = region_id)
    cities = region.city_set.all()
    return render(request, "Travel/region_city.html", {'cities': cities})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/Travel')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

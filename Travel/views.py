# -*- coding: utf-8 -*- #
from django.shortcuts import render, redirect

from . models import Manager, Tourist, Country, City, Tour, Region

from django.contrib.auth import login, authenticate
from Travel.forms import SignUpForm

def index(request):
    return render(request, "Travel/index.html", { "Travel": True })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/Travel')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def regions(request):
    region = Region.objects.all()
    return render(request, "Travel/regions.html", {'region': region, 'regions': True})

def region_city(request, region_id = None):
    region = Region.objects.get(id = region_id)
    cities = region.city_set.all()
    return render(request, "Travel/region_city.html", {'cities': cities})

def tour(request, tour_id = None, region_id = None):
    tour = Tour.objects.filter(id = tour_id)
    return render(request, 'Travel/tour.html', {'tour': tour})

# -*- coding: utf-8 -*- #
from django.shortcuts import render, redirect

from . models import *

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
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def regions(request):
    region = Region.objects.all()
    return render(request, "Travel/regions.html", {'region': region, 'regions': True})

def region_cities(request, region_id):
    region = Region.objects.get(id=region_id)
    cities = region.city_set.all()
    return render(request, "Travel/region_cities.html", {'cities': cities, 'regions':True})

def tour(request, tour_id):
    tour = Tour.objects.get(id = tour_id)
    tourist__id=request.user.tourist.id
    try:
        booking=Tourbooking.objects.get(tour__id=tour_id, tourist__id=tourist__id)
    except Tourbooking.DoesNotExist:
        booking = None
    return render(request, 'Travel/tour.html', {'tour': tour, 'booking': booking})

def add_book_tour(request, tour_id):
    t = Tour.objects.get(id=tour_id)
    tourist=request.user.tourist
    Tourbooking.objects.create(tour=t, tourist=tourist)
    return redirect('tour', tour_id=tour_id)

def delete_book_tour(request, tour_id):
    t = Tour.objects.get(id=tour_id)    
    tourist=request.user.tourist.id
    Tourbooking.objects.get(tour=t, tourist=tourist).delete()
    return redirect('tour', tour_id=tour_id)
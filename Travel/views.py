# -*- coding: utf-8 -*- #
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Travel.forms import SignUpForm, UpdateProfile
from . models import *

def index(request):
    return render(request, "Travel/index.html", {"Travel":True})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('my_profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def regions(request):
    region=Region.objects.all()
    return render(request, "Travel/regions.html", {'region': region, 'regions': True})

def region_cities(request, region_id):
    region=Region.objects.get(id=region_id)
    cities=region.city_set.all()
    return render(request, "Travel/region_cities.html", {"cities": cities, "regions":True})

def tour(request, tour_id):
    tour = Tour.objects.get(id = tour_id)
    booking=None
    if not request.user.is_anonymous:
        tourist_id=request.user.tourist.id
        try:
            booking=Tour_booking.objects.get(tour__id=tour_id, tourist__id=tourist_id)
        except Tour_booking.DoesNotExist:
            pass
    return render(request, 'Travel/tour.html', {'tour': tour, 'booking': booking, "regions":True})

def my_profile(request):
    tourist=request.user.tourist
    return render(request, 'Travel/my_profile.html', {'my_profile':True})

def change_my_profile(request):
    if request.method == 'POST':
        change_profile = UpdateProfile(request.POST, instance=request.user)
        change_data = UpdateProfile(request.POST, instance=request.user.tourist)
        if change_profile.is_valid() and change_data.is_valid():
            change_profile.save()
            change_data.save()
            request.user.tourist.patronymic
            request.user.tourist.mobile_phone
            return redirect('my_profile')
    else:
        change_profile = UpdateProfile()
        change_data = UpdateProfile()
    return render(request, 'registration/change_my_profile.html', {'my_profile':True})

def my_tours(request):
    tourist_id=request.user.tourist.id
    booking=Tour_booking.objects.all().filter(tourist__id=tourist_id)
    return render(request, 'Travel/my_tours.html', {'booking':booking, 'my_tours':True})

def add_booking_tour(request, tour_id):
    tour=Tour.objects.get(id=tour_id)
    tourist=request.user.tourist
    Tour_booking.objects.create(tour=tour, tourist=tourist)
    return redirect('my_tours')

def delete_booking_tour(request, tour_id):
    tour=Tour.objects.get(id=tour_id)
    tourist=request.user.tourist
    Tour_booking.objects.get(tour=tour, tourist=tourist).delete()
    return redirect('my_tours')

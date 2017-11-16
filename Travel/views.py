# -*- coding: utf-8 -*- #
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Travel.forms import SignupForm, ChangeForm
from . models import *

def home(request):
    return render(request, 'Travel/home.html', {'Travel':True})

def regions(request):
    countries=Country.objects.all()
    return render(request, "Travel/regions.html", {'countries':countries})

def cities(request, region_id):
    region=Region.objects.get(id=region_id)
    cities=region.city_set.all()
    return render(request, "Travel/cities.html", {"cities": cities})

def tours(request, tour_id):
    tour = Tour.objects.get(id = tour_id)
    # Цена за тур и гостиницу по скидке 
    discount_price=(tour.days*tour.hotel_price+tour.tour_price)*(100-tour.discount)/100
    # Цена за тур и гостиницу без скидки 
    price=tour.days*tour.hotel_price+tour.tour_price
    # Цена за тур без гостиницы cо скидкой
    discount_tour_price=tour.tour_price*(100-tour.discount)/100
    booking=None
    if not request.user.is_anonymous:
        tourist_id=request.user.tourist.id
        try:
            booking=TourBooking.objects.get(tour__id=tour_id, tourist__id=tourist_id)
        except TourBooking.DoesNotExist:
            pass
    return render(request, 
        'Travel/tour.html', 
        {'tour': tour,
            'discount_price': discount_price,
            'price': price, 
            'discount_tour_price': discount_tour_price,
            'booking': booking,
        }
    )

def discount_tours(request):
    discount_tours = Tour.objects.all().exclude(discount = 0)
    return render(request, 'Travel/discount_tours.html', {'discount_tours':discount_tours})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('my_profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def my_profile(request):
    tourist=request.user.tourist
    return render(request, 'Travel/my_profile.html', {'my_profile':True})

def change_profile(request):
    if request.method == 'POST':
        change_profile = ChangeForm(request.POST, instance=request.user)
        change_data = ChangeForm(request.POST, instance=request.user.tourist)
        if change_profile.is_valid() and change_data.is_valid():
            change_profile.save()
            change_data.save()
            request.user.tourist.patronymic
            request.user.tourist.phone
            return redirect('my_profile')
    else:
        change_profile = ChangeForm()
        change_data = ChangeForm()
    return render(request, 'registration/change_profile.html', {'my_profile':True})

def my_tours(request):
    tourist_id=request.user.tourist.id
    booking=TourBooking.objects.all().filter(tourist__id=tourist_id)
    return render(request, 'Travel/my_tours.html', {'booking':booking, 'my_tours':True})

def add_booking_tour(request, tour_id):
    tour=Tour.objects.get(id=tour_id)
    tourist=request.user.tourist
    last_name = request.user.last_name
    first_name = request.user.first_name
    patronymic = request.user.tourist.patronymic
    phone = request.user.tourist.phone
    TourBooking.objects.create(tour=tour, tourist=tourist, last_name=last_name, first_name=first_name, patronymic=patronymic, phone=phone)
    return redirect('my_tours')

def delete_booking_tour(request, tour_id):
    tour=Tour.objects.get(id=tour_id)
    tourist=request.user.tourist
    TourBooking.objects.get(tour=tour, tourist=tourist).delete()
    return redirect('my_tours')

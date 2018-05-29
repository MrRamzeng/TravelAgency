from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Travel.forms import SignupForm, EditForm
from Travel.models import *

def index(request):
    return render(
        request, 
        "Travel/index.html", 
        {
            "Travel": True
        }
    )
def regions(request):
    regions = Region.objects.all()
    return render(
        request, 
        "Travel/regions.html", 
        {
            "regions": regions
        }
    )

def cities(request, region_id):
    region = Region.objects.get(id = region_id)
    cities = region.city_set.all()
    return render(
        request, 
        "Travel/cities.html", 
        {
            "cities": cities
        }
    )

def tours(request, tour_id):
    tour = Tour.objects.get(id = tour_id)
    # Цена за тур и гостиницу по скидке 
    discount_price = (tour.days * tour.hotel_price + tour.tour_price) * (100 - tour.discount) / 100
    # Цена за тур и гостиницу без скидки 
    price = tour.days * tour.hotel_price + tour.tour_price
    # Цена за тур без гостиницы cо скидкой
    discount_tour_price = tour.tour_price * (100 - tour.discount) / 100
    booking = None
    if not request.user.is_anonymous:
        tourist_id = request.user.tourist.id
        try:
            booking = TourBooking.objects.get(
                tour__id = tour_id, 
                tourist__id = tourist_id
            )
        except TourBooking.DoesNotExist:
            pass
    return render(request, 
        "Travel/tour.html", 
        {
            "tour": tour,
            "discount_price": discount_price,
            "price": price, 
            "discount_tour_price": discount_tour_price,
            "booking": booking,
        }
    )

def discount_tours(request):
    discount_tours = Tour.objects.all().exclude(discount = 0)
    return render(
        request, 
        "Travel/discount_tours.html", 
        {
            "discount_tours": discount_tours
        }
    )

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(
                username = username, 
                password = raw_password
            )
            login(request, user)
            return redirect("edit_profile")
    else:
        form = SignupForm()
    return render(
        request, 
        "registration/signup.html", 
        {
            "form": form
        }
    )

def profile(request):
    tourist = request.user.tourist
    return render(
        request, 
        "Travel/profile.html", 
        {
            "profile": True
        }
    )

def edit_profile(request):
    if request.method == "POST":
        edit_user = EditForm(
            request.POST, 
            instance = request.user
        )
        edit_profile = EditForm(
            request.POST, 
            instance = request.user.tourist
        )
        if edit_user.is_valid() and edit_profile.is_valid():
            edit_user.save()
            edit_profile.save()
            request.user.tourist.patronymic
            #request.user.tourist.birthday
            request.user.tourist.phone
            return redirect("profile")
    else:
        edit_user = EditForm()
        edit_profile = EditForm()
    return render(
        request, 
        "registration/edit_profile.html",
        {
            "edit_user": edit_user, 
            "edit_profile": edit_profile
        }
    )

def bookings(request):
    tourist_id = request.user.tourist.id
    booking = TourBooking.objects.all().filter(tourist__id = tourist_id)
    return render(
        request, 
        "Travel/bookings.html", 
        {
            "booking": booking, 
            "bookings": True
        }
    )

def add_booking(request, tour_id):
    tour = Tour.objects.get(id = tour_id)
    tourist = request.user.tourist
    last_name = request.user.last_name
    first_name = request.user.first_name
    patronymic = request.user.tourist.patronymic
    phone = request.user.tourist.phone
    TourBooking.objects.create(
        tour = tour, 
        tourist = tourist, 
        last_name = last_name, 
        first_name = first_name, 
        patronymic = patronymic, 
        phone = phone
    )
    return redirect("bookings")

def delete_booking(request, tour_id):
    tour = Tour.objects.get(id = tour_id)
    tourist = request.user.tourist
    TourBooking.objects.get(tour = tour, tourist = tourist).delete()
    return redirect("bookings")

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
            return redirect('edit_profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    tourist=request.user.tourist
    return render(request, 'Travel/profile.html', {'profile':True})

def edit_profile(request):
    if request.method == 'POST':
        edit_user = EditForm(request.POST, instance=request.user)
        edit_profile = EditForm(request.POST, instance=request.user.tourist)
        if edit_user.is_valid() and edit_profile.is_valid():
            edit_user.save()
            edit_profile.save()
            request.user.tourist.patronymic
            #request.user.tourist.birthday
            request.user.tourist.phone
            return redirect('profile')
    else:
        edit_user = EditForm()
        edit_profile = EditForm()
    return render(request, 'registration/edit_profile.html', {'edit_user': edit_user, 'edit_profile': edit_profile})

def bookings(request):
    tourist_id=request.user.tourist.id
    booking=TourBooking.objects.all().filter(tourist__id=tourist_id)
    return render(request, 'Travel/bookings.html', {'booking':booking, 'bookings':True})

def add_booking(request, tour_id):
    tour=Tour.objects.get(id=tour_id)
    tourist=request.user.tourist
    last_name = request.user.last_name
    first_name = request.user.first_name
    patronymic = request.user.tourist.patronymic
    phone = request.user.tourist.phone
    TourBooking.objects.create(tour=tour, tourist=tourist, last_name=last_name, first_name=first_name, patronymic=patronymic, phone=phone)
    return redirect('bookings')

def delete_booking(request, tour_id):
    tour=Tour.objects.get(id=tour_id)
    tourist=request.user.tourist
    TourBooking.objects.get(tour=tour, tourist=tourist).delete()
    return redirect('bookings')

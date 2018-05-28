from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name = "index"),
#    url(r"^countries/$", views.countries, name = "countries"),
    url(r"^regions/$", views.regions, name = "regions"),
    url(r"^cities/(?P<region_id>[0-9]+)/$", views.cities, name = "cities"),
    url(r"^tour/(?P<tour_id>[0-9]+)/$", views.tours, name = "tours"),
    url(r"^discount_tours/$", views.discount_tours, name = "discount_tours"),
    url(r"^profile/$", views.profile, name="profile"),
    url(r"^bookings/$", views.bookings, name="bookings"),
    url(r"^add_booking/(?P<tour_id>[0-9]+)/$", views.add_booking, name = "add_booking"),
    url(r"^delete_booking/(?P<tour_id>[0-9]+)/$", views.delete_booking, name = "delete_booking")
]
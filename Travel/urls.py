from django.conf.urls import url
from Travel import views as Travel_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^regions/$', views.regions, name = "regions"),
    url(r'^cities/(?P<region_id>[0-9]+)/$', views.cities, name = "cities"),
    url(r'^tour/(?P<tour_id>[0-9]+)/$', views.tours, name = 'tours'),
    url(r'^discount_tours/$', views.discount_tours, name = 'discount_tours'),
    url(r'^signup/$', Travel_views.signup, name='signup'),
    url(r'^change_profile$', Travel_views.change_profile, name='change_profile'),
    url(r'^my_profile/$', views.my_profile, name='my_profile'),
    url(r'^my_tours/$', views.my_tours, name='my_tours'),
    url(r'^add_booking_tour/(?P<tour_id>[0-9]+)/$', views.add_booking_tour, name = 'add_booking_tour'),
    url(r'^delete_booking_tour/(?P<tour_id>[0-9]+)/$', views.delete_booking_tour, name = 'delete_booking_tour')
]
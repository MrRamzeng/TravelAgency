from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^regions/$', views.regions, name = "regions"),
    url(r'^cities/(?P<region_id>[0-9]+)/$', views.region_cities, name = "region_cities"),
    url(r'^tour/(?P<tour_id>[0-9]+)/$', views.tour, name = 'tour'),
    url(r'^my_profile/$', views.my_profile, name='my_profile'),
    url(r'^my_tours/$', views.my_tours, name='my_tours'),
    url(r'^add_booking_tour/(?P<tour_id>[0-9]+)/$', views.add_booking_tour, name = 'add_booking_tour'),
    url(r'^delete_booking_tour/(?P<tour_id>[0-9]+)/$', views.delete_booking_tour, name = 'delete_booking_tour')
]
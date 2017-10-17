from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^regions/$', views.regions, name = "regions"),
    url(r'^cities/(?P<region_id>[0-9]+)/$', views.region_cities, name = "region_cities"),
    url(r'^tour/(?P<tour_id>[0-9]+)/$', views.tour, name = 'tour'),
    url(r'^add_booking/(?P<tour_id>[0-9]+)/$', views.add_book_tour, name = 'add_booking'),
    url(r'^delete_booking/(?P<tour_id>[0-9]+)/$', views.delete_book_tour, name = 'delete_booking')
]
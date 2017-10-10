from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^regions/$', views.regions, name = "regions"),
    url(r'^regions/region_city/(?P<region_id>[0-9]+)/$', views.region_city, name = "region_city"),
    url(r'^regions/region_city/(?P<region_id>[0-9]+)/tour/(?P<tour_id>[0-9]+)/$', views.tour, name = 'tour'),
]
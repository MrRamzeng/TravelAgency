from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^regions/$', views.regions, name = "regions"),
    url(r'^regions/region_city/$', views.region_city, name = 'region_city_without_id'),
    url(r'^regions/region_city/(?P<region_id>[0-9]+)/$', views.region_city, name = "region_city"),
]
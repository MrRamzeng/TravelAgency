# -*- coding: utf-8 -*- #
from django.contrib import admin
from django.contrib.auth.models import User
from . models import Country, Region, City, Hotel, Type_of_tour, Tour,  Manager, Tourist, Type_of_allocution, Allocution, Tour_booking

#Здесь происходит регистрация моделей

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Type_of_tour)
admin.site.register(Tour)
admin.site.register(Manager)
admin.site.register(Tourist)
admin.site.register(Type_of_allocution)
admin.site.register(Allocution)
admin.site.register(Tour_booking)

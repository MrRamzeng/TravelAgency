# -*- coding: utf-8 -*- #
from django.contrib import admin
from django.contrib.auth.models import User
from . models import Manager, Tourist, Country, City, Type_of_tour, Tour, Region, Tour_booking, Hotel

#Здесь происходит регистрация моделей

admin.site.register(Manager)
admin.site.register(Tourist)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Type_of_tour)
admin.site.register(Tour)
admin.site.register(Region)
admin.site.register(Tour_booking)
admin.site.register(Hotel)
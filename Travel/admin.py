# -*- coding: utf-8 -*- #
from django.contrib import admin

from . models import Manager, Tourist, Country, City, Tour, Region, Tourbooking, Recource, Type, Hotel

#Здесь происходит регистрация моделей

admin.site.register(Manager)
admin.site.register(Tourist)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Tour)
admin.site.register(Region)
admin.site.register(Tourbooking)
admin.site.register(Recource)
admin.site.register(Type)
admin.site.register(Hotel)
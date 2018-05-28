# -*- coding: utf-8 -*- #
from django.contrib import admin
from . models import Country, Region, City, Hotel, TourType, Tour,  Manager, Tourist, TourBooking

# Здесь происходит регистрация моделей 
class SearchTour(admin.ModelAdmin): # Поиск туров
    search_fields=['name', 'city__name', 'hotel__name', 'type__name']

class SearchManager(admin.ModelAdmin): # Поиск менеджеров
    search_fields=['username__last_name', 'username__first_name', 'patronymic', 'phone']

class SearchTourist(admin.ModelAdmin): # Поиск туристов 
    search_fields=['username__last_name', 'username__first_name', 'patronymic', 'phone']

class SearchBooking(admin.ModelAdmin): # Поиск бронирований туров
    search_fields=['tour__name', 'last_name', 'first_name', 'patronymic', 'phone']

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(TourType)
admin.site.register(Tour, SearchTour)
admin.site.register(Manager, SearchManager)
admin.site.register(Tourist, SearchTourist)
admin.site.register(TourBooking, SearchBooking)
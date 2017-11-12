# -*- coding: utf-8 -*- #
from django.contrib import admin
from . models import Country, Region, City, Hotel, Tour_type, Tour,  Manager, Tourist, Recource_type, Recource, Tour_booking

# Здесь происходит регистрация моделей 
class Search_tour(admin.ModelAdmin): # Поиск туров
    search_fields=['type__name','name','city__name', 'hotel__name', 'type__name']

class Search_manager(admin.ModelAdmin): # Поиск менеджеров
    search_fields=['username__last_name', 'username__first_name', 'patronymic', 'phone']

class Search_tourist(admin.ModelAdmin): # Поиск туристов 
    search_fields=['username__last_name', 'username__first_name', 'patronymic', 'phone']

class Search_recource(admin.ModelAdmin): # Поиск обращений туристов
    search_fields=['last_name', 'first_name', 'patronymic', 'type__name']

class Search_tour_booking(admin.ModelAdmin): # Поиск бронирований туров
    search_fields=['tour__name', 'last_name', 'first_name', 'patronymic', 'phone']

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Tour_type)
admin.site.register(Tour, Search_tour)
admin.site.register(Manager, Search_manager)
admin.site.register(Tourist, Search_tourist)
admin.site.register(Recource_type)
admin.site.register(Recource, Search_recource)
admin.site.register(Tour_booking, Search_tour_booking)
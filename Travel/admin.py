# -*- coding: utf-8 -*- #
from django.contrib import admin
from django.contrib.auth.models import User
from . models import Country, Region, City, Hotel, Type_of_tour, Tour,  Manager, Tourist, Type_of_allocution, Allocution, Tour_booking

#Здесь происходит регистрация моделей

class Search_allocation(admin.ModelAdmin):
    search_fields=[
        'last_name', 
        'first_name', 
        'patronymic', 
        'type_of_allocution__name'
    ]
class Search_tourist(admin.ModelAdmin):
    search_fields=[
        'username__last_name',
        'username__first_name',
        'patronymic',
        'mobile_phone',
    ]

class Search_manager(admin.ModelAdmin):
    search_fields=[
        'username__last_name',
        'username__first_name',
        'patronymic',
        'mobile_phone',
    ]

class Search_tour(admin.ModelAdmin):
    search_fields=[
        'type__name',
        'name',
        'city__name',
        'hotel__name',
    ]
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Type_of_tour)
admin.site.register(Tour, Search_tour)
admin.site.register(Manager, Search_manager)
admin.site.register(Tourist, Search_tourist)
admin.site.register(Type_of_allocution)
admin.site.register(Allocution, Search_allocation)
admin.site.register(Tour_booking)


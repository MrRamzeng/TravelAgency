# -*- coding: utf-8 -*- #
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
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
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class Tourist(admin.StackedInline):
    model = Tourist
    can_delete = False
    verbose_name_plural = 'Турист'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Tourist, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)
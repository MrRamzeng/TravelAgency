# -*- coding: utf-8 -*- #
from django.contrib import admin
from . models import Region, City, Hotel, TourType, Tour,  Manager,  TourBooking
import django.contrib.auth.admin
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings

# Здесь происходит регистрация моделей 
class SearchTour(admin.ModelAdmin): # Поиск туров
    search_fields=['name', 'date',]
    list_per_page = 10


class SearchManager(admin.ModelAdmin): # Поиск менеджеров
    search_fields=['username__last_name', 'username__first_name', 'patronymic', 'phone']
    list_per_page = 10

class SearchBooking(admin.ModelAdmin): # Поиск бронирований туров
    search_fields=['tour__name', 'last_name', 'first_name', 'patronymic', 'phone', 'tour__name', 'tour__date']
    readonly_fields=['last_name', 'first_name', 'patronymic', 'phone', 'tour']
    list_per_page = 10
    list_display=[
        'tourist', 'tour', 'approved', 'cancel'
    ]
    exclude=['tourist',]
    def save_model(self, request, obj, form, change):
        if request.user.is_staff:
            settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            settings.EMAIL_HOST = 'smtp.yandex.ru'
            settings.EMAIL_PORT = 587
            settings.EMAIL_HOST_USER = 'manager.ostrovoktour@ya.ru'
            settings.EMAIL_HOST_PASSWORD = 'AzegKovvdar142'
            settings.EMAIL_USE_TLS = True
        if obj.approved == True:
            message = ("Уважаемый " + str(obj.tourist.username) + ', заявка на тур: "'
            + str(obj.tour.name)
            + '" одобрена.')
            send_mail(
                subject="Статус вашей заявки изменился",
                message=message,
                from_email='manager.ostrovoktour@ya.ru',
                recipient_list=[str(obj.tourist.username.email)],
                html_message=message,
                fail_silently=False,
            )
        elif obj.cancel == True:
            message = "Уважаемый " + str(obj.tourist.username) + ", к сожалению ваша заявка отклонена. <br>" + '"' + str(obj.message) + '"'
            send_mail(
                subject="Статус вашей заявки изменился",
                message=message,
                from_email='manager.ostrovoktour@ya.ru',
                recipient_list=[str(obj.tourist.username.email)],
                html_message=message,
                fail_silently=False,
            )
        super().save_model(request, obj, form, change)

class AdminTourType(admin.ModelAdmin):
    list_per_page = 10

class AdminRegion(admin.ModelAdmin):
    list_per_page = 10

class AdminCity(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'region']

class AdminHotel(admin.ModelAdmin):
    list_display = ['name', 'phone', 'city']
    search_fields = ['name', 'city__name']
    list_filter = ['name', 'city__name']
    ordering = ('city__name',)
    list_per_page = 10

admin.site.register(Region, AdminRegion)
admin.site.unregister(auth.models.Group)
admin.site.register(City, AdminCity)
admin.site.register(Hotel, AdminHotel)
admin.site.register(TourType, AdminTourType)
admin.site.register(Tour, SearchTour)
admin.site.register(Manager, SearchManager)
admin.site.register(TourBooking, SearchBooking)
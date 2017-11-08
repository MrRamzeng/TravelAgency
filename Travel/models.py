# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

def user_unicode_patch(self):
    return '%s, %s %s' % (self.username, self.last_name, self.first_name)

User.__unicode__ = user_unicode_patch

# Create your models here.

class Country(models.Model):
    name = models.CharField('Страна', max_length=50)
    def __unicode__(self):
        return unicode(self.name)
    class Meta:
        verbose_name_plural="страны"
        verbose_name="страна"

class Region(models.Model):
    country = models.ForeignKey(Country, verbose_name="Страна", null=True, on_delete=models.SET_NULL)
    name = models.CharField('Регион', max_length=50)
    def __unicode__(self):
        return unicode(self.country) + ", " + unicode(self.name)
    class Meta:
        verbose_name_plural="регионы"
        verbose_name="регион"

class City(models.Model):
    region = models.ForeignKey(Region, verbose_name="Регион", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField('Город', max_length=50)
    def __unicode__(self):
        return unicode(self.region) + ", " + unicode(self.name)
    class Meta:
        verbose_name_plural="города"
        verbose_name="город"

class Hotel(models.Model):
    name = models.CharField('Название', max_length=50)
    city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=models.SET_NULL)
    address = models.CharField('Адрес', max_length=200)
    comfort = models.PositiveIntegerField('Комфорт', default=1)
    def __unicode__(self):
        return (unicode(self.city)
            + ", " 
            + unicode(self.address) 
            + ", " 
            +  unicode(self.name) 
            + ", звезд: " 
            + unicode(self.comfort)
        )
    class Meta:
        verbose_name_plural="отели"
        verbose_name="отель"

class Type_of_tour(models.Model):
    name = models.CharField('Тип тура', max_length=50)
    def __unicode__(self):
        return unicode(self.name)
    class Meta: 
        verbose_name_plural = 'типы тура'
        verbose_name = 'тип тура'

class Tour(models.Model):
    type = models.ForeignKey(Type_of_tour, null=True, on_delete=models.SET_NULL, verbose_name='Тип тура')
    name = models.CharField('Название тура', max_length=50)
    tour_description = models.TextField('Описание тура')
    city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=models.SET_NULL)
    date = models.DateField('Дата тура')
    days = models.PositiveIntegerField('Дней')
    hotel = models.ForeignKey(Hotel, verbose_name="Отель", null=True, blank=True)
    hotel_price = models.PositiveIntegerField('Цена за номер', null=True, blank=True)
    tour_price = models.PositiveIntegerField('Цена')
    discount = models.PositiveIntegerField('Скидка', default=0)
    def __unicode__(self):
        if self.discount > 0:
            if self.hotel is None:
                price = (self.tour_price) * (100 - self.discount) / 100
            else:
                price = (self.hotel_price * self.days + self.tour_price) * (100 - self.discount) / 100
        else:
            if self.hotel is None:
                price = (self.tour_price)
            else:
                price = (self.hotel_price * self.days + self.tour_price)
        if self.hotel is None:
            if self.discount == 0:
                return (unicode(self.name)
                    + ", г." 
                    + unicode(self.city.name)
                    + ", тип тура: " 
                    + unicode(self.type) 
                    + ", " 
                    + unicode(self.date.strftime("%d.%m.%Y")) 
                    + ", дней: " 
                    + unicode(self.days) 
                    + ", " 
                    + unicode(int(price)) 
                    + " руб."
                )
            else:
                return (unicode(self.name)
                    + ", г." 
                    + unicode(self.city.name)
                    + ", тип тура: " 
                    + unicode(self.type) 
                    + ", " 
                    + unicode(self.date.strftime("%d.%m.%Y")) 
                    + ", дней: " 
                    + unicode(self.days) 
                    + ", скидка: " 
                    + unicode(self.discount)
                    + "%, " 
                    + unicode(int(price)) 
                    + " руб."
                )
        else:
            if self.discount == 0:
                return (unicode(self.name)
                    + ", г." 
                    + unicode(self.city.name)
                    + ", тип тура: "
                    + unicode(self.type)
                    + ", " 
                    + unicode(self.date.strftime("%d.%m.%Y"))
                    + ", дней: "
                    + unicode(self.days) 
                    + ", " 
                    + unicode(self.hotel.name) 
                    + ", " 
                    + unicode(int(price)) 
                    + "руб."
                )
            else:
                return (unicode(self.name)
                    + ", г." 
                    + unicode(self.city.name)
                    + ", тип тура: "
                    + unicode(self.type)
                    + ", " 
                    + unicode(self.date.strftime("%d.%m.%Y"))
                    + ", дней: "
                    + unicode(self.days) 
                    + ", " 
                    + unicode(self.hotel.name) 
                    + ", скидка: " 
                    + unicode(self.discount)
                    + "%, " 
                    + unicode(int(price)) 
                    + "руб."
                )
    class Meta:
        verbose_name_plural = "туры"
        verbose_name = 'тур'

class Manager(models.Model):
    username = models.OneToOneField(User, verbose_name="Пользователь", null=True, on_delete=models.SET_NULL)
    patronymic = models.CharField('Отчество', blank=True, max_length=50)
    date_of_birth = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=200)
    mobile_phone = models.CharField('Номер телефона', max_length=50)
    def __unicode__(self):
        return (unicode(self.username) 
            + " "
            + unicode(self.patronymic)
            + ", дата рождения: " 
            + unicode(self.date_of_birth.strftime("%d.%m.%Y")) 
            + " "
            + unicode(self.mobile_phone)
        )
    class Meta:
        verbose_name_plural="менеджеры"
        verbose_name='менеджер'

class Tourist(models.Model):
    username = models.OneToOneField(User, verbose_name="Пользователь", null=True, on_delete=models.SET_NULL)
    patronymic = models.CharField('Отчество', blank=True, max_length=50)
    mobile_phone = models.CharField('Номер телефона', max_length=50)
    def __unicode__(self):
        return (unicode(self.username) 
            + " "
            + unicode(self.patronymic)
            + ", "
            + unicode(self.mobile_phone)
        )
    class Meta:
        verbose_name_plural="туристы"
        verbose_name='турист'

class Type_of_allocution(models.Model):
    name = models.CharField('тип обращения', max_length=50)
    def __unicode__(self):
        return unicode(self.name)
    class Meta:
        verbose_name = 'тип обращения'
        verbose_name_plural = 'типы обращений'

class Allocution(models.Model):
    username = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)
    type_of_allocution = models.ForeignKey(Type_of_allocution, null=True, on_delete=models.SET_NULL, verbose_name='Тип обращения')
    text_allocution = models.TextField('Текст обращения')
    date_and_time = models.DateTimeField('Дата и время обращения')
    comments = models.TextField('Комментарии')
    tour = models.ForeignKey(Tour, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Выбранный тур')
    def __unicode__(self):
        if self.patronymic is "":
            return (unicode(self.last_name)
                + ' ' 
                + unicode(self.first_name) 
                + ', тип обращения: ' 
                + unicode(self.type_of_allocution) 
                + ', дата время обращения: ' 
                + unicode(self.date_and_time.strftime("%d.%m.%Y, %H:%M"))
                + ', тур: '
                + unicode(self.tour.name)
            )
        else:
            return (unicode(self.last_name)
                + ' '
                + unicode(self.first_name) 
                + ' ' 
                + unicode(self.patronymic) 
                + ', тип обращения: ' 
                + unicode(self.type_of_allocution) 
                + ', дата и время обращения: ' 
                + unicode(self.date_and_time.strftime("%d.%m.%Y, %H:%M"))
                + ', тур: '
                + unicode(self.tour.name)
            )
    class Meta:
        verbose_name_plural='обращения'
        verbose_name='обращение'

class Tour_booking(models.Model):
    tour = models.ForeignKey(Tour, verbose_name="Выбранный тур", null=True, on_delete=models.SET_NULL)
    tourist = models.ForeignKey(Tourist, verbose_name="Турист", blank=True, null=True, on_delete=models.SET_NULL)
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)
    manager = models.ForeignKey(Manager, verbose_name="Менеджер", null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False, verbose_name='Подтвержение')
    def __unicode__(self):
        if self.approved is True:
            return (unicode(self.tour)
                + ", " 
                + unicode(self.tourist) 
                + ", подтверждено"
            )
        else:
            return (unicode(self.tour)
                + ", " 
                + unicode(self.tourist) 
                + ", не подтверждено"
            )
    class Meta:
        verbose_name = "бронирование тура"
        verbose_name_plural="броонирования туров"

@receiver(post_save, sender=User)
def create_tourist(sender, instance, created, **kwargs):
    if created:
        Tourist.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_tourist(sender, instance, **kwargs):
    instance.tourist.save()

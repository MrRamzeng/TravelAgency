# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Manager(models.Model): # Модель менеджера
    username = models.OneToOneField(User, on_delete=models.CASCADE) # Индивидуальный идентификатор пользователя
    birthday = models.DateField("Дата рождения") # Дата рождения 
    phone = models.CharField("Номер телефона", max_length = 100) # Мобильный телефон
    adress = models.CharField("Адрес", max_length = 100) # Адрес проживания
    def __unicode__(self):
        return unicode(self.username)
    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

class Country(models.Model):
    name = models.CharField("Страна", max_length = 50)
    def __unicode__(self):
        return unicode(self.name)
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Region(models.Model):
    country = models.ForeignKey(Country, null = True, on_delete = models.SET_NULL, verbose_name = "Страна")
    name = models.CharField("Регион", max_length = 50)
    def __unicode__(self):
        return unicode(self.name)
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class City(models.Model):
    region = models.ForeignKey(Region, null = True, on_delete = models.SET_NULL, verbose_name = "Выберите область")
    name = models.CharField("Город", max_length = 50)
    def __unicode__(self):
        return unicode(self.region) + ", " + unicode(self.name)
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Hotel(models.Model):
    name = models.CharField('Название', max_length = 50, blank = True, null = True)
    city = models.ForeignKey(City, null = True, on_delete = models.SET_NULL, verbose_name = "Город")
    address = models.TextField('Адрес')
    comfort = models.IntegerField('Звезд')
    def __unicode__(self):
        return unicode(self.name) + ', ' + unicode(self.city) + ' ' + unicode(self.address) + ' Звезд: ' + unicode(self.comfort)
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        
class Tour(models.Model): 
    name = models.CharField('Название тура', max_length = 50) 
    city = models.ForeignKey(City, null = True, on_delete = models.SET_NULL, verbose_name = "Город")
    hotel = models.ForeignKey(Hotel, blank = True, null = True, on_delete = models.SET_NULL, verbose_name = 'Отель')
    date = models.DateField("Дата заезда") 
    days = models.IntegerField('Количество дней') 
    price = models.IntegerField("Цена путевки")
    text = models.TextField('Описание')
    def __unicode__(self):
        return unicode(self.name) + ' ' + unicode(self.city) + " " + unicode(self.date) + ', ' + unicode(self.days) + " дней, " + unicode(self.price) + "руб."
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

class Tourist(models.Model): # Модель пользователя сайта (туриста)
    username = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    phone = models.CharField("Номер телефона", max_length = 100) # Мобильный телефон
    def __unicode__(self):
        return unicode(self.username)
    class Meta:
        verbose_name = 'Турист'
        verbose_name_plural = 'Туристы'

class Type(models.Model):
    name = models.CharField("Тип", max_length = 50)
    def __unicode__(self):
        return unicode(self.name)
    class Meta:
        verbose_name = 'Тип обращения'
        verbose_name_plural = 'Типы обращений'

class Recource(models.Model):
    tourist = models.ForeignKey(Tourist, null = True, on_delete = models.SET_NULL, verbose_name = 'Турист')
    date_time = models.DateTimeField('Дата и время заявки')
    resource_text = models.TextField('Текст обращения')
    type_resource = models.ForeignKey(Type, null = True, on_delete = models.SET_NULL, verbose_name = 'Тип обращения')
    comment = models.TextField('Комментрарии')
    tour = models.ForeignKey(Tour, null = True, on_delete = models.SET_NULL, verbose_name = "Тур")
    def __unicode__(self):
        return unicode(self.tourist) + ', ' + unicode(self.date_time)
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

class Tour_booking(models.Model):
    tour = models.ForeignKey(Tour, null = True, on_delete = models.SET_NULL, verbose_name = "Выбранный тур")
    tourist = models.ForeignKey(Tourist, null = True, on_delete = models.SET_NULL, verbose_name = "Турист")
    manager = models.ForeignKey(Manager, null = True, on_delete = models.SET_NULL, verbose_name = 'Менеджер')
    approved = models.BooleanField(default = False, verbose_name = 'Подтверждение')
    def __unicode__(self):
        return unicode(self.tourist) + ', ' + unicode(self.tour) + ', ' + unicode(self.approved)
    class Meta:
        verbose_name = 'Бронирование тура'
        verbose_name_plural = 'Бронирование туров'

@receiver(post_save, sender=User)
def create_tourist(sender, instance, created, **kwargs):
    if created:
        Tourist.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_tourist(sender, instance, **kwargs):
    instance.tourist.save()

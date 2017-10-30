# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

# Create your models here.
class Country(models.Model):
	name = models.CharField('Страна', max_length=50)
	def __unicode__(self):
		return unicode(self.name)
	class Meta:
		verbose_name_plural="Страны"

class Region(models.Model):
	country = models.ForeignKey(Country, verbose_name="Страна", null=True, on_delete=models.SET_NULL)
	name = models.CharField('Регион', max_length=50)
	def __unicode__(self):
		return unicode(self.country) + ", " + unicode(self.name)
	class Meta:
		verbose_name_plural="Регионы"

class City(models.Model):
	region = models.ForeignKey(Region, verbose_name="Регион", null=True, blank=True, on_delete=models.SET_NULL)
	name = models.CharField('Город', max_length=50)
	def __unicode__(self):
		return unicode(self.region) + ", " + unicode(self.name)
	class Meta:
		verbose_name_plural="Города"

class Hotel(models.Model):
	name = models.CharField('Название', max_length=50)
	city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=models.SET_NULL)
	address = models.CharField('Адрес', max_length=200)
	comfort = models.IntegerField('Комфорт')
	def __unicode__(self):
		return unicode(self.name) + ", " + unicode(self.city) + ", звезд: " + unicode(self.comfort)
	class Meta:
		verbose_name_plural="Отели"

class Type_of_tour(models.Model):
    name = models.CharField('Тип тура', max_length=50)
    def __unicode__(self):
    	return unicode(self.name)
    class Meta: 
        verbose_name_plural = 'Типы тура'
        verbose_name = 'тип тура'

class Tour(models.Model):
    type = models.ForeignKey(Type_of_tour, null=True, on_delete=models.SET_NULL, verbose_name='Тип тура')
    name = models.CharField('Название тура', max_length=50)
    tour_description = models.TextField('Описание тура')
    city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=models.SET_NULL)
    date = models.DateField('Дата заезда')
    days = models.IntegerField('Дней')
    hotel = models.ForeignKey(Hotel, verbose_name="Отель", null=True, on_delete=models.SET_NULL, blank=True)
    price = models.IntegerField('Цена')
    def __unicode__(self):
        return unicode(self.name) + ", тип тура: " + unicode(self.type) + ", " + unicode(self.date) + ", " + unicode(self.days) + ", звезд: " + unicode(self.hotel) + ", " + unicode(self.price) + " руб."
    class Meta:
		verbose_name_plural = "Туры"
		verbose_name = 'Тур'

class Manager(models.Model):
	username = models.OneToOneField(User, verbose_name="Пользователь", null=True, on_delete=models.SET_NULL)
	date_of_birth = models.DateField('Дата рождения')
	address = models.CharField('Адрес', max_length=200)
	mobile_phone = models.CharField('Номер телефона', max_length=50)
	def __unicode__(self):
		return unicode(self.user)
	class Meta:
		verbose_name_plural="Менеджеры"

class Tourist(models.Model):
	username = models.OneToOneField(User, verbose_name="Пользователь", null=True, on_delete=models.SET_NULL)
	def __unicode__(self):
		return unicode(self.user)
	class Meta:
		verbose_name_plural="Туристы"

class Tour_booking(models.Model):
	tour = models.ForeignKey(Tour, verbose_name="Выбранный тур", null=True, on_delete=models.SET_NULL)
	tourist = models.ForeignKey(Tourist, verbose_name="Турист", null=True, on_delete=models.SET_NULL)
	manager = models.ForeignKey(Manager, verbose_name="Менеджер", null=True, on_delete=models.SET_NULL)
	approved = models.BooleanField(default=False, verbose_name='Подтвержение')
	def __unicode__(self):
		return unicode(self.tour) + ", " + unicode(self.tourist) + ", " + unicode(self.manager) + ", " + unicode(self.approved)
	class Meta:
		verbose_name = "Бронирование тура"
		verbose_name_plural="Броонирования туров"

@receiver(post_save, sender=User)
def create_tourist(sender, instance, created, **kwargs):
	if created:
		Tourist.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_tourist(sender, instance, **kwargs):
	instance.tourist.save()

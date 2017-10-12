# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Manager(models.Model): # Модель менеджера
	user = models.OneToOneField(User, on_delete = models.CASCADE) # Индивидуальный идентификатор пользователя 
	surname = models.CharField("Фамилия", max_length = 20) # Фамилия 
	name = models.CharField("Имя", max_length = 20) # Имя 
	patronymic = models.CharField("Отчество", max_length = 20) # Отчество
	birthday = models.DateField("Дата рождения") # Дата рождения 
	phone = models.CharField("Номер телефона", max_length = 100) # Мобильный телефон
	adress = models.CharField("Адрес", max_length = 100) # Адрес проживания
	def __unicode__(self):
		full_name = unicode(self.surname) + " " + unicode(self.name[0]) + "." + unicode(self.patronymic[0])
		return full_name

class Country(models.Model):
	name = models.CharField("Страна", max_length = 50)
	def __unicode__(self):
		return unicode(self.name)

class Region(models.Model):
	country = models.ForeignKey(Country, null = True, on_delete = models.SET_NULL, verbose_name = "Страна")
	name = models.CharField("Регион", max_length = 50)
	def __unicode__(self):
		return unicode(self.name)

class City(models.Model):
	region = models.ForeignKey(Region, null = True, on_delete = models.SET_NULL, verbose_name = "Выберите область")
	name = models.CharField("Город", max_length = 50)
	def __unicode__(self):
		return unicode(self.name) + ", " + unicode(self.region)

class Hotel(models.Model):
	name = models.CharField('Название', max_length = 50, blank = True, null = True)
	city = models.ForeignKey(City, null = True, on_delete = models.SET_NULL, verbose_name = "Город")
	address = models.TextField('Адрес')
	comfort = models.IntegerField('Звезд')
	def __unicode__(self):
		return 'Гостиница ' + unicode (self.name) + ', ' + unicode(self.city) + ' ' + unicode(self.address) + ' Звезд: ' + unicode(self.comfort)

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

class Tourist(models.Model): # Модель пользователя сайта (туриста)
	user = models.ForeignKey(User, on_delete = models.CASCADE) # Индивидуальный идентификатор пользователя
	surname = models.CharField("Фамилия", max_length = 20) # Фамилия 
	name = models.CharField("Имя", max_length = 20) # Имя 
	patronymic = models.CharField("Отчество", max_length = 20) # Отчество
	birthday = models.DateField("Дата рождения") # Дата рождения 
	phone = models.CharField("Номер телефона", max_length = 100) # Мобильный телефон
	adress = models.CharField("Адрес", max_length = 100) # Адрес проживания
	def __unicode__(self):
		full_name = unicode(self.surname) + " " + unicode(self.name[0]) + "." + unicode(self.patronymic[0]) + "."
		return full_name

class Type(models.Model):
	name = models.CharField("Тип", max_length = 50)
	def __unicode__(self):
		return unicode(self.name)

class Recource(models.Model):
	tourist = models.ForeignKey(Tourist, null = True, on_delete = models.SET_NULL, verbose_name = 'Турист')
	date_time = models.DateTimeField('Дата и время заявки')
	resource_text = models.TextField('Текст обращения')
	type_resource = models.ForeignKey(Type, null = True, on_delete = models.SET_NULL, verbose_name = 'Тип обращения')
	comment = models.TextField('Комментрарии')
	tour = models.ForeignKey(Tour, null = True, on_delete = models.SET_NULL, verbose_name = "Тур")
	def __unicode__(self):
		return unicode(self.tourist) + ' ' + unicode(self.date_time)

class Tourbooking(models.Model):
	tour = models.ForeignKey(Tour, null = True, on_delete = models.SET_NULL, verbose_name = "Выбранный тур")
	tourist = models.ForeignKey(Tourist, null = True, on_delete = models.SET_NULL, verbose_name = "Турист")
	manager = models.ForeignKey(Manager, null = True, on_delete = models.SET_NULL, verbose_name = 'Менеджер')
	approved = models.BooleanField(default = False, verbose_name = 'Подтверждение')
	def __unicode__(self):
		return unicode(self.tourist) + ', ' + unicode(self.tour) + ', ' + unicode(self.approved)
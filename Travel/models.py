# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.core.validators import MaxValueValidator

# Создание моделей.
class Country(models.Model):
	name = models.CharField('Страна', max_length=50)
	def __unicode__(self):
		return unicode(self.name)
	class Meta:
		verbose_name_plural="Страны"
		verbose_name="страна"

class Region(models.Model):
	country = models.ForeignKey(Country, verbose_name="Страна", null=True, on_delete=models.SET_NULL)
	name = models.CharField('Регион', max_length=50)
	def __unicode__(self):
		return unicode(self.country) + ", " + unicode(self.name)
	class Meta:
		verbose_name_plural="Регионы"
		verbose_name="регион"

class City(models.Model):
	region = models.ForeignKey(Region, verbose_name="Регион", null=True, blank=True, on_delete=models.SET_NULL)
	name = models.CharField('Город', max_length=50)
	def __unicode__(self):
		return unicode(self.region) + ", " + unicode(self.name)
	class Meta:
		verbose_name_plural="Города"
		verbose_name="город"

class Hotel(models.Model):
	name = models.CharField('Название', max_length=50)
	city = models.ForeignKey(City, verbose_name="Город", null=True, on_delete=models.SET_NULL)
	address = models.CharField('Адрес', max_length=200)
	comfort = models.PositiveIntegerField('Комфорт', default=1, validators=[MaxValueValidator(5)])
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
		verbose_name_plural="Гостиницы"
		verbose_name="гостиница"

class Tour_type(models.Model):
	name = models.CharField('Тип тура', max_length=50)
	def __unicode__(self):
		return unicode(self.name)
	class Meta: 
		verbose_name_plural = 'Типы тура'
		verbose_name = 'тип тура'

class Tour(models.Model):
	name = models.CharField('Название тура', max_length=50)
	tour_type = models.ForeignKey(Tour_type, null=True, verbose_name='Тип тура')
	tour_description = models.TextField('Описание тура')
	city = models.ForeignKey(City, null=True, verbose_name='Город')
	tour_date = models.DateField('Дата тура')
	tour_days = models.PositiveIntegerField('Дней', default=1)
	hotel = models.ForeignKey(Hotel, null=True, blank=True, verbose_name='Гостиница')
	hotel_price = models.PositiveIntegerField('Цена за номер', default=0)
	tour_price = models.PositiveIntegerField('Цена тура', default=0)
	discount = models.PositiveIntegerField('Скидка', default=0, validators=[MaxValueValidator(100)])
	def __unicode__(self):
		if self.discount>0:
			if self.hotel is None:
				price=self.tour_price*(100-self.discount)/100
			else:
				price=(self.tour_price+self.hotel_price*self.tour_days)*(100-self.discount)/100
		else:
			if self.hotel is None:
				price=self.tour_price
			else:
				price=self.tour_price+self.hotel_price*self.tour_days
		if self.discount==0:
			if self.hotel is None:
				return (
					unicode(self.name)
					+ ', тип тура: '
					+  unicode(self.tour_type)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.tour_date.strftime('%d.%m.%Y'))
					+ ', дней: '
					+ unicode(self.tour_days)
					+ ', цена: '
					+ unicode(int(price))
					+ 'руб.'
				)
			else:
				return (
					unicode(self.name)
					+ ', тип тура: '
					+  unicode(self.tour_type)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.tour_date.strftime('%d.%m.%Y'))
					+ ', гостиница: '
					+ unicode(self.hotel.name)
					+ ', дней: '
					+ unicode(self.tour_days)
					+ ', цена: '
					+ unicode(int(price))
					+ 'руб.'
				)
		else:
			if self.hotel is None:
				return (
					unicode(self.name)
					+ ', тип тура: '
					+  unicode(self.tour_type)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.tour_date.strftime('%d.%m.%Y'))
					+ ', дней: '
					+ unicode(self.tour_days)
					+ ', скидка: '
					+ unicode(self.discount)
					+ '%, цена: '
					+ unicode(int(price))
					+ 'руб.'
				)
			else:
				return (
					unicode(self.name)
					+ ', тип тура: '
					+  unicode(self.tour_type)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.tour_date.strftime('%d.%m.%Y'))
					+ ', дней: '
					+ unicode(self.tour_days)
					+ ', гостиница: '
					+ unicode(self.hotel.name)
					+ ', скидка: '
					+ unicode(self.discount)
					+ '%, цена: '
					+ unicode(int(price))
					+ 'руб.'
				)
	class Meta:
		verbose_name_plural='Туры'
		verbose_name='тур'

class Manager(models.Model):
	username = models.OneToOneField(User, verbose_name="Пользователь")
	patronymic = models.CharField('Отчество', blank=True, max_length=50)
	birthday = models.DateField('Дата рождения')
	address = models.CharField('Адрес', max_length=200)
	phone_number = models.CharField('Номер телефона', max_length=50)
	def __unicode__(self):
		return (unicode(self.username) 
			+ " "
			+ unicode(self.patronymic)
			+ ", дата рождения: " 
			+ unicode(self.birthday.strftime("%d.%m.%Y")) 
			+ " "
			+ unicode(self.phone_number)
		)
	class Meta:
		verbose_name_plural="Менеджеры"
		verbose_name='менеджер'

class Tourist(models.Model):
	username = models.OneToOneField(User, verbose_name="Пользователь")
	patronymic = models.CharField('Отчество', blank=True, max_length=50)
	phone_number = models.CharField('Номер телефона', max_length=50)
	def __unicode__(self):
		return (unicode(self.username) 
			+ " "
			+ unicode(self.patronymic)
		)
	class Meta:
		verbose_name_plural="Туристы"
		verbose_name='турист'

class Allocution_type(models.Model):
	name = models.CharField('тип обращения', max_length=50)
	def __unicode__(self):
		return unicode(self.name)
	class Meta:
		verbose_name_plural = 'Типы обращений'
		verbose_name = 'тип обращения'

class Allocution(models.Model):
	username = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
	last_name = models.CharField('Фамилия', max_length=50)
	first_name = models.CharField('Имя', max_length=50)
	patronymic = models.CharField('Отчество', max_length=50, blank=True)
	allocution_type = models.ForeignKey(Allocution_type, null=True, on_delete=models.SET_NULL, verbose_name='Тип обращения')
	text_allocution = models.TextField('Текст обращения')
	date_and_time = models.DateTimeField('Дата и время обращения')
	comments = models.TextField('Комментарии')	
	tour = models.ForeignKey(Tour, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Выбранный тур')
	def __unicode__(self):
		if self.patronymic is "": # Если нет фамилии
			return (unicode(self.last_name)
				+ ' ' 
				+ unicode(self.first_name) 
				+ ', тип обращения: ' 
				+ unicode(self.allocution_type) 
				+ ', дата время обращения: ' 
				+ unicode(self.date_and_time.strftime("%d.%m.%Y, %H:%M"))
				+ ', тур: '
				+ unicode(self.tour.name)
			)
		else: # Иначе
			return (unicode(self.last_name)
				+ ' '
				+ unicode(self.first_name) 
				+ ' ' 
				+ unicode(self.patronymic) 
				+ ', тип обращения: ' 
				+ unicode(self.allocution_type) 
				+ ', дата и время обращения: ' 
				+ unicode(self.date_and_time.strftime("%d.%m.%Y, %H:%M"))
				+ ', тур: '
				+ unicode(self.tour.name)
			)
	class Meta:
		verbose_name_plural='Обращения'
		verbose_name='обращение'

class Tour_booking(models.Model):
	tour = models.ForeignKey(Tour, verbose_name="Выбранный тур")
	tourist = models.ForeignKey(Tourist, verbose_name="Турист", blank=True)
	last_name = models.CharField('Фамилия', max_length=50, blank=True)
	first_name = models.CharField('Имя', max_length=50, blank=True)
	patronymic = models.CharField('Отчество', max_length=50, blank=True)
	phone_number = models.CharField('Номер телефона', max_length=50)
	manager = models.ForeignKey(Manager, verbose_name="Менеджер", null=True)
	approved = models.BooleanField(default=False, verbose_name='Подтвержение')
	def __unicode__(self):
		if self.tourist:
			if self.approved is True: # Если подтверждено
				return (unicode(self.tour)
					+ ", " 
					+ unicode(self.tourist) 
					+ " "
					+ unicode(self.phone_number)
					+ ", подтверждено"
				)
			else: # Иначе
				return (unicode(self.tour)
					+ ", " 
					+ unicode(self.tourist) 
					+ " "
					+ unicode(self.phone_number)
					+ ", не подтверждено"
				)
		else:
			if self.approved is True: # Если подтверждено
				return (unicode(self.tour)
					+ ", " 
					+ unicode(self.last_name) 
					+ " "
					+ unicode(self.first_name)
					+ " "
					+ unicode(self.patronymic)
					+ ", "
					+ unicode(self.phone_number)
					+ ", подтверждено"
				)
			else: # Иначе
				return (unicode(self.tour)
					+ ", " 
					+ unicode(self.last_name) 
					+ " "
					+ unicode(self.first_name)
					+ " "
					+ unicode(self.patronymic)
					+ ", "
					+ unicode(self.phone_number)
					+ ", не подтверждено"
				)
	class Meta:
		verbose_name_plural="Бронирования туров"
		verbose_name = "бронирование тура"

@receiver(post_save, sender=User)
def create_tourist(sender, instance, created, **kwargs):
	if created:
		Tourist.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_tourist(sender, instance, **kwargs):
	instance.tourist.save()

def user_unicode_patch(self):
	return '%s, %s %s' % (self.username, self.last_name, self.first_name)

User.__unicode__ = user_unicode_patch

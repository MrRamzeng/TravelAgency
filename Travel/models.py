# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

# Создание моделей.
class Country(models.Model):
	name = models.CharField('Страна', max_length=50)
	def __unicode__(self):
		return unicode(self.name)
	class Meta:
		verbose_name_plural="Страны"
		verbose_name="страна"

class Region(models.Model):
	country = models.ForeignKey(Country, verbose_name="Страна", null=True)
	name = models.CharField('Регион', max_length=50)
	def __unicode__(self):
		return unicode(self.country) + ", " + unicode(self.name)
	class Meta:
		verbose_name_plural="Регионы"
		verbose_name="регион"

class City(models.Model):
	region = models.ForeignKey(Region, verbose_name="Регион", null=True, blank=True)
	name = models.CharField('Город', max_length=50)
	def __unicode__(self):
		return unicode(self.region) + ", " + unicode(self.name)
	class Meta:
		verbose_name_plural="Города"
		verbose_name="город"

class Hotel(models.Model):
	name = models.CharField('Название', max_length=50)
	city = models.ForeignKey(City, verbose_name="Город", null=True)
	address = models.CharField('Адрес', max_length=200)
	comfort = models.PositiveIntegerField('Комфорт', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
	def __unicode__(self):
		return (unicode(self.city.name)
			+ ", " 
			+ unicode(self.address) 
			+ ", " 
			+  unicode(self.name) 
			+ ", звезд: " 
			+ unicode(self.comfort))
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
	type = models.ForeignKey(Tour_type, null=True, verbose_name='Тип тура')
	description = models.TextField('Описание тура')
	city = models.ForeignKey(City, null=True, verbose_name='Город')
	date = models.DateField('Дата тура')
	days = models.PositiveIntegerField('Дней', default=1, validators=[MinValueValidator(1)])
	hotel = models.ForeignKey(Hotel, null=True, blank=True, verbose_name='Гостиница')
	hotel_price = models.PositiveIntegerField('Цена за номер', default=0)
	tour_price = models.PositiveIntegerField('Цена тура', default=0)
	discount = models.PositiveIntegerField('Скидка', default=0, validators=[MaxValueValidator(100)])
	def __unicode__(self):
		if self.discount>0:
			if self.hotel is None:
				price=self.tour_price*(100-self.discount)/100
				return (
					unicode(self.name)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.date.strftime('%d.%m.%Y'))
					+ ', скидка: '
					+ unicode(self.discount)
					+ '%, '
					+ unicode(int(price))
					+ 'руб.')
			else:
				price=(self.tour_price+self.hotel_price*self.days)*(100-self.discount)/100
				return (
					unicode(self.name)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.date.strftime('%d.%m.%Y'))
					+ ', '
					+ unicode(self.hotel.name)
					+ ', скидка: '
					+ unicode(self.discount)
					+ '%, '
					+ unicode(int(price))
					+ 'руб.')
		else:
			if self.hotel is None:
				return (
					unicode(self.name)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.date.strftime('%d.%m.%Y'))
					+ ', '
					+ unicode(self.tour_price)
					+ 'руб.')
			else:
				price=self.tour_price+self.hotel_price*self.days
				return (
					unicode(self.name)
					+ ', г. '
					+ unicode(self.city.name)
					+ ', дата тура: '
					+ unicode(self.date.strftime('%d.%m.%Y'))
					+ ', '
					+ unicode(self.hotel.name)
					+ ', '
					+ unicode(int(price))
					+ 'руб.')
	class Meta:
		verbose_name_plural='Туры'
		verbose_name='тур'

class Manager(models.Model):
	username = models.OneToOneField(User, verbose_name="Пользователь")
	patronymic = models.CharField('Отчество', blank=True, max_length=50)
	birthday = models.DateField('Дата рождения')
	address = models.CharField('Адрес', max_length=200)
	phone = models.CharField('Номер телефона', max_length=50)
	def __unicode__(self):
		return (unicode(self.username) 
			+ " "
			+ unicode(self.patronymic)
			+ ", дата рождения: " 
			+ unicode(self.birthday.strftime("%d.%m.%Y")) 
			+ " "
			+ unicode(self.phone))
	class Meta:
		verbose_name_plural="Менеджеры"
		verbose_name='менеджер'

class Tourist(models.Model):
	username = models.OneToOneField(User, verbose_name="Пользователь")
	patronymic = models.CharField('Отчество', blank=True, max_length=50)
	phone = models.CharField('Номер телефона', max_length=50)
	def __unicode__(self):
		return (
			unicode(self.username) 
			+ " "
			+ unicode(self.patronymic)
			+ ' '
			+ unicode(self.phone))
	class Meta:
		verbose_name_plural="Туристы"
		verbose_name='турист'

class Recource_type(models.Model):
	name = models.CharField('тип обращения', max_length=50)
	def __unicode__(self):
		return unicode(self.name)
	class Meta:
		verbose_name_plural = 'Типы обращений'
		verbose_name = 'тип обращения'

class Recource(models.Model):
	last_name = models.CharField('Фамилия', max_length=50)
	first_name = models.CharField('Имя', max_length=50)
	patronymic = models.CharField('Отчество', max_length=50, blank=True)
	tour = models.ForeignKey(Tour, null=True, blank=True, verbose_name='Выбранный тур')
	type = models.ForeignKey(Recource_type, null=True, verbose_name='Тип обращения')
	text = models.TextField('Текст обращения')
	date_and_time = models.DateTimeField('Дата и время обращения')
	comments = models.TextField('Комментарии')	
	def __unicode__(self):
		if self.tour:
			return (
				unicode(self.last_name)
				+ ' '
				+ unicode(self.first_name) 
				+ ' ' 
				+ unicode(self.patronymic) 
				+ ', тип обращения: ' 
				+ unicode(self.type) 
				+ ', дата и время обращения: ' 
				+ unicode(self.date_and_time.strftime("%d.%m.%Y, %H:%M"))
				+ ', тур: '
				+ unicode(self.tour))
		else:
			return (
				unicode(self.last_name)
				+ ' '
				+ unicode(self.first_name) 
				+ ' ' 
				+ unicode(self.patronymic) 
				+ ', тип обращения: ' 
				+ unicode(self.type) 
				+ ', дата и время обращения: ' 
				+ unicode(self.date_and_time.strftime("%d.%m.%Y, %H:%M")))
	class Meta:
		verbose_name_plural='Обращения'
		verbose_name='обращение'

class Tour_booking(models.Model):
	tour = models.ForeignKey(Tour, verbose_name="Выбранный тур")
	tourist = models.ForeignKey(Tourist, verbose_name="Турист", blank=True)
	last_name = models.CharField('Фамилия', max_length=50)
	first_name = models.CharField('Имя', max_length=50)
	patronymic = models.CharField('Отчество', max_length=50, blank=True)
	phone = models.CharField('Номер телефона', max_length=50)
	manager = models.ForeignKey(Manager, verbose_name="Менеджер", null=True)
	approved = models.BooleanField(default=False, verbose_name='Подтвержение')
	def __unicode__(self):
		if self.approved is True: # Если подтверждено
			return (unicode(self.last_name) 
				+ " "
				+ unicode(self.first_name)
				+ " "
				+ unicode(self.patronymic)
				+ ", "
				+ unicode(self.phone)
				+ ", " 
				+ unicode(self.tour.name)
				+ ", подтверждено")
		else: # Иначе
			return (
				unicode(self.last_name) 
				+ " "
				+ unicode(self.first_name)
				+ " "
				+ unicode(self.patronymic)
				+ ", " 
				+ unicode(self.phone)
				+ ", "
				+ unicode(self.tour.name)
				+ ", не подтверждено")
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

def user_full_name(self):
	return '%s, %s %s' % (self.username, self.last_name, self.first_name)

User.__unicode__ = user_full_name

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Создание моделей.
class Region(models.Model):
    name = models.CharField('Регион', max_length=50)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural="Регионы"
        verbose_name="регион"

class City(models.Model):
    region = models.ForeignKey(Region, verbose_name="Регион", null=True, blank=True)
    name = models.CharField('Населенный пункт', max_length=50)
    def __str__(self):
        return str(self.region) + ", " + str(self.name)
    class Meta:
        verbose_name_plural="населенные пункты"
        verbose_name="населенный пункт"

class Hotel(models.Model):
    name = models.CharField('Название', max_length=50)
    phone_regex = RegexValidator(regex=r'^\+7\s[(]{1}[0-9]{3}[)]{1}\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')
    phone = models.CharField('Телефон', validators=[phone_regex], max_length=20, blank=True)
    comfort = models.PositiveIntegerField('Комфорт', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    city = models.ForeignKey(City, verbose_name="Населенный пункт", null=True)
    address = models.CharField('Адрес', max_length=200)
    def __str__(self):
        return (str(self.name)
            + ", звезд: "
            + str(self.comfort)
            + ", г." 
            + str(self.city.name)
            + ", " 
            + str(self.address))
    class Meta:
        verbose_name_plural="гостиницы"
        verbose_name="гостиница"

class TourType(models.Model):
    name = models.CharField('Тип тура', max_length=50)
    def __str__(self):
        return str(self.name)
    class Meta: 
        verbose_name_plural = 'Типы тура'
        verbose_name = 'тип тура'

class Tour(models.Model):
    name = models.CharField('Название тура', max_length=50)
    type = models.ForeignKey(TourType, null=True, verbose_name='Тип тура')
    description = RichTextUploadingField('Описание тура')
    city = models.ForeignKey(City, null=True, verbose_name='Населенный пункт')
    date = models.DateField('Дата тура')
    days = models.PositiveIntegerField('Дней', default=1, validators=[MinValueValidator(1)])
    hotel = models.ForeignKey(Hotel, null=True, blank=True, verbose_name='Гостиница')
    hotel_price = models.PositiveIntegerField('Цена за номер', default=0)
    tour_price = models.PositiveIntegerField('Цена тура', default=0)
    discount = models.PositiveIntegerField('Скидка', default=0, validators=[MaxValueValidator(100)])
    def __str__(self):
        if self.discount>0:
            if self.hotel is None:
                price=self.tour_price*(100-self.discount)/100
                return (
                    str(self.name)
                    + ', '
                    + str(self.date.strftime('%d.%m.%Y'))
                    + ', дней: '
                    + str(self.days)
                    + ', скидка: '
                    + str(self.discount)
                    + '%, '
                    + str(int(price))
                    + 'руб.')
            else:
                price=(self.tour_price+self.hotel_price*self.days)*(100-self.discount)/100
                return (
                    str(self.name)
                    + ', '
                    + str(self.date.strftime('%d.%m.%Y'))
                    + ', дней: '
                    + str(self.days)
                    + ', '
                    + str(self.hotel.name)
                    + ', скидка: '
                    + str(self.discount)
                    + '%, '
                    + str(int(price))
                    + 'руб.')
        else:
            if self.hotel is None:
                return (
                    str(self.name)
                    + ', '
                    + str(self.date.strftime('%d.%m.%Y'))
                    + ', дней: '
                    + str(self.days)
                    + ', '
                    + str(self.tour_price)
                    + 'руб.')
            else:
                price=self.tour_price+self.hotel_price*self.days
                return (
                    str(self.name)
                    + ', '
                    + str(self.date.strftime('%d.%m.%Y'))
                    + ', дней: '
                    + str(self.days)
                    + ', '
                    + str(self.hotel.name)
                    + ', '
                    + str(int(price))
                    + 'руб.')
    class Meta:
        verbose_name_plural='Туры'
        verbose_name='тур'

class Manager(models.Model):
    username = models.OneToOneField(User, verbose_name="Пользователь")
    patronymic = models.CharField('Отчество', blank=True, max_length=50)
    birthday = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=200)
    phone_regex = RegexValidator(regex=r'^\+7\s[(]{1}[0-9]{3}[)]{1}\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')
    phone = models.CharField('Телефон', validators=[phone_regex], max_length=20, blank=True)
    def __str__(self):
        return (str(self.username) 
            + " "
            + str(self.patronymic)
            + ", дата рождения: " 
            + str(self.birthday.strftime("%d.%m.%Y")) 
            + ", "
            + str(self.phone))
    class Meta:
        verbose_name_plural="Менеджеры"
        verbose_name='менеджер'

class Tourist(models.Model):
    username = models.OneToOneField(User, verbose_name="Пользователь")
    patronymic = models.CharField('Отчество', blank=True, max_length=50)
#    birthday = models.DateField('Дата рождения', blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+7\s[(]{1}[0-9]{3}[)]{1}\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')
    phone = models.CharField('Телефон', validators=[phone_regex], max_length=20, blank=True)
    def __str__(self):
        return (
            str(self.username) 
            + " "
            + str(self.patronymic)
            #+ ", дата рождения: " 
            #+ str(self.birthday.strftime("%d.%m.%Y")) 
            + ', '
            + str(self.phone))
    class Meta:
        verbose_name_plural="Туристы"
        verbose_name='турист'

class TourBooking(models.Model):
    tourist = models.ForeignKey(Tourist, blank=True, verbose_name='Турист')
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', blank=True, max_length=50)
    phone_regex = RegexValidator(regex=r'^\+7\s[(]{1}[0-9]{3}[)]{1}\s[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{2}$')
    phone = models.CharField('Телефон', validators=[phone_regex], max_length=20, blank=True)
    tour = models.ForeignKey(Tour, null=True, verbose_name='Выбранный тур')
    manager = models.ForeignKey(Manager, null=True, verbose_name='менеджер')
    approved = models.BooleanField(default=False, verbose_name='Подтверждение')
    cancel = models.BooleanField(default=False, blank=True, verbose_name='Отмена')
    message = models.CharField('Причина отмены', max_length=50, blank=True)
    def __str__(self):
        if self.approved is True:
            return (str(self.last_name)
                + ' '
                + str(self.first_name)
                + ' '
                + str(self.patronymic)
                + ', '
                + str(self.phone)
                + ', '
                + str(self.tour)
                + ', подтверждено')
        elif self.cancel is True:
            return (str(self.last_name)
                + ' '
                + str(self.first_name)
                + ' '
                + str(self.patronymic)
                + ', '
                + str(self.phone)
                + ', '
                + str(self.tour)
                + 'отменено. '
                + str(self.message))
        else:
            return (str(self.last_name)
                + ' '
                + str(self.first_name)
                + ' '
                + str(self.patronymic)
                + ', '
                + str(self.phone)
                + ', '
                + str(self.tour)
                + ', не подтверждено')
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
    return '%s %s' % (self.last_name, self.first_name)

User.__str__ = user_full_name

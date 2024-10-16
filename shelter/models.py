from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'null': True, 'blank': True}


class Pet(models.Model):
    animal = models.CharField(max_length=100, verbose_name='Животное')
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    description = models.CharField(max_length=100, verbose_name='Описание')
    health = models.CharField(max_length=100, verbose_name='Здоровье')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение',
                              default='/media/images/default_image.jpg', **NULLABLE)

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return self.name


class Shelter(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = PhoneNumberField(default='+7', verbose_name='Номер телефона', **NULLABLE)
    country = CountryField(default='RU', verbose_name='Страна', blank_label='(select country)', **NULLABLE)
    places = models.CharField(max_length=100, verbose_name='Количество мест в приюте')

    class Meta:
        verbose_name = 'Приют'
        verbose_name_plural = 'Приюты'

    def __str__(self):
        return self.title

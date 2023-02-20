from django.db import models
from django.utils.datetime_safe import date


class Products(models.Model):
    product_title = models.CharField(verbose_name='название продукта', max_length=100, unique=True)
    model = models.CharField(verbose_name='модель продукта', max_length=100)
    date_release = models.DateField(verbose_name='дата релиза продукта', default=date.today)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"


class Contacts(models.Model):
    email = models.EmailField(verbose_name='email', blank=True)
    country = models.CharField(verbose_name='страна', max_length=30)
    city = models.CharField(verbose_name='город', max_length=30)
    street = models.CharField(verbose_name='улица', max_length=50)
    home_number = models.PositiveIntegerField(verbose_name='номер дома')

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.home_number}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"


class Sales(models.Model):
    class Meta:
        verbose_name = 'сеть по продаже'
        verbose_name_plural = "сети продаж"

    class Chain(models.IntegerChoices):
        factory = 1, 'завод'
        retail = 2, 'розничная сеть'
        individual_entrepreneur = 3, 'индивидуальный предприниматель'

    chain_link = models.PositiveSmallIntegerField(verbose_name='звено цепи', choices=Chain.choices)
    title = models.CharField(verbose_name='название фирмы', max_length=100, unique=True)
    contacts = models.ForeignKey(Contacts, verbose_name='контакты', on_delete=models.CASCADE)
    products = models.ForeignKey(Products, verbose_name='продукты', on_delete=models.CASCADE)
    providers = models.CharField(max_length=30, verbose_name='поставщик', blank=True)
    arrears = models.DecimalField(verbose_name='задолженность перед поставщиком', max_digits=8, decimal_places=2)
    creation_time = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

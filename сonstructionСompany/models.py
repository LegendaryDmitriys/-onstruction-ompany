from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User, Permission


class Address(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return self.address

class Personnel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, verbose_name='Должность')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, verbose_name='Адрес')
    experience = models.IntegerField(verbose_name='Стаж')

    def __str__(self):
        return self.full_name

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

class Order(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Адрес')
    completion_date = models.DateField(verbose_name='Дата завершения')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE, verbose_name='Персонал')
    
    def __str__(self):
        return f"{self.project.name} - {self.address.address}"

class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес')
    quantity = models.IntegerField(verbose_name='Количество')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cтоимость')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    purchase = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Закупка')

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал')

    def __str__(self):
        return f"{self.material.name} - Количество: {self.material.quantity}, Вес: {self.material.weight}, Стоимость: {self.material.cost}, Закупка: {self.material.purchase}"




from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    position = models.CharField(max_length=50)
    passport = models.CharField(max_length=10)


class Soft(models.Model):
    soft_name = models.CharField(max_length=20)
    employee = models.ManyToManyField(Employee, related_name='employee_soft')


class Documents(models.Model):
    document = models.CharField(max_length=20)
    soft = models.ManyToManyField(Soft, related_name='documents')


class Resource(models.Model):
    name = models.CharField(max_length=20)
    soft = models.ManyToManyField(Soft, related_name='soft')
    employee = models.ManyToManyField(Employee, related_name='employee_resource')

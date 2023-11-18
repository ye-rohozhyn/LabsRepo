from django.db import models


class Client(models.Model):
    ClientCompany = models.CharField(max_length=255)
    CheckingAccount = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=15)
    ContactPerson = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)


class Car(models.Model):
    CarBrand = models.CharField(max_length=255)
    CarPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Repair(models.Model):
    StartDate = models.DateField()
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    RepairType = models.CharField(max_length=255)
    OneHourPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Discount = models.DecimalField(max_digits=4, decimal_places=2)
    Hours = models.DecimalField(max_digits=6, decimal_places=2)
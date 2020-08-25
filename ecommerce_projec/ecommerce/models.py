from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Customer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=8, default=Decimal(0.0))
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, through='PurchaseProducts', through_fields=('purchase', 'product'))
    iva = models.DecimalField(max_digits=20, decimal_places=8, default=Decimal(0.0))
    subtotal = models.DecimalField(max_digits=20, decimal_places=8, default=Decimal(0.0))
    total = models.DecimalField(max_digits=20, decimal_places=8, default=Decimal(0.0))


class PurchaseProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser',
    )


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100, default="Customer Customer")
    email = models.EmailField(unique=True, default='customer@customer.com')
    phone = models.CharField(max_length=15, default=1234569870)

    def __str__(self):
        return self.name


class Billing(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"Billing for {self.customer}"


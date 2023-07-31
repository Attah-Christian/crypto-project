from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.


class Enquirie(models.Model):
    btc_wallet = models.CharField(max_length=100)
    eth_wallet = models.CharField(max_length=100)
    usdterc20_wallet = models.CharField(max_length=100)
    usdttrc20_wallet =models.CharField(max_length=100)

class Number(models.Model):
    balance = models.CharField(max_length=100, blank=True)
    profit1 = models.CharField(max_length=100, blank=True)
    profit2 = models.CharField(max_length=100, blank=True)
    profit3 = models.CharField(max_length=100, blank=True)
    profit4 = models.CharField(max_length=100, blank=True)
    profit5 = models.CharField(max_length=100, blank=True)


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class CurrencyExchangeRates(models.Model):
    base = models.CharField(max_length=3)
    target = models.CharField(max_length=3)
    exchange_rate = models.FloatField()
    fetch_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.base} to {self.target} date: {self.eate}"
 
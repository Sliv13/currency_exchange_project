from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Currency(models.Model):
    code=models.CharField(max_length=3,unique=True)
    class Meta:
        ordering=('code',)
class CurrencyExchangeRates(models.Model):
    base = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base')
    target = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='target')
    exchange_rate = models.FloatField()
    fetch_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.base} to {self.target} date: {self.eate}"
 

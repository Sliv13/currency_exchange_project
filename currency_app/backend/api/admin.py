from django.contrib import admin
from .models import CurrencyExchangeRates

# Register your models here.


class CERFilter(admin.ModelAdmin):
    list_display=['base','target','exchange_rate','fetch_date']
    readonly_fields=['base','target','exchange_rate','fetch_date']
    ordering=('base','target','-fetch_date')
    search_fields=['base__exact','target__exact']

admin.site.register(CurrencyExchangeRates,CERFilter)
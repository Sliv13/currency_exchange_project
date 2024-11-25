from django.contrib import admin
from .models import CurrencyExchangeRates,Currency

# Register your models here.
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields=('code')
    ordering=('code')
class CERFilter(admin.ModelAdmin):
    list_display=['base_code','target_code','exchange_rate','fetch_date']
    readonly_fields=['base','target','exchange_rate','fetch_date']
    ordering=('base__code','target__code','-fetch_date')
    search_fields=['base__code__exact','target__code__exact']
    
    def base_code(self, obj):
        return obj.base.code

    def target_code(self, obj):
        return obj.target.code
    
    
admin.site.register(CurrencyExchangeRates,CERFilter)
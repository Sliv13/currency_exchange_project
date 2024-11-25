from .models import CurrencyExchangeRates,Currency
from rest_framework import serializers

class Currencies_Exchange_Serializer(serializers.ModelSerializer):
    
    currency_pair=serializers.SerializerMethodField()
    class Meta:
        model=CurrencyExchangeRates
        fields=['currency_pair','exchange_rate']
    
    
    def get_currency_pair(self, obj):
        return f"{obj.base.code}{obj.target.code}"
        

class Currencies_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Currency
        fields=['code']
    
    
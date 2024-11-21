from .models import CurrencyExchangeRates
from rest_framework import serializers

class Currencies_Exchange_Serializer(serializers.ModelSerializer):
    
    currency_pair=serializers.SerializerMethodField()
    class Meta:
        model=CurrencyExchangeRates
        fields=['currency_pair','exchange_rate']
    
    
    def get_currency_pair(self, obj):
        return f"{obj.base}{obj.target}"
        

class Currencies_Serializer(serializers.Serializer):
    code = serializers.SerializerMethodField()
    
    def get_codes(self,obj):
        return obj
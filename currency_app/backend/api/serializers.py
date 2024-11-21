from .models import CurrencyExchangeRates
from rest_framework import serializers

class Currencies_Exchange_Serializer(serializers.ModelSerializer):
    
    currency_pair=serializers.SerializerMethodField()
    class Meta:
        model=CurrencyExchangeRates
        fields=['currency_pair','exchange_rate']
    
    
    def get_currency_pair(self, obj):
        return f"{obj.base}{obj.target}"
        
# class Currencies_Serializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         # Call the original method to get serialized data
#         data = super().to_representation(data)
#         # Prepend custom words to each item
#         return [f"Item: {item}" for item in data]
    
class Currencies_Serializer(serializers.Serializer):
    code = serializers.SerializerMethodField()
    
    def get_codes(self,obj):
        return obj
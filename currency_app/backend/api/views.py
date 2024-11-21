from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CurrencyExchangeRates
from .serializers import Currencies_Serializer,Currencies_Exchange_Serializer
from rest_framework import status

class Get_Exchange_Rates(APIView):
    def get(self, request, base, target):
        
        latest_rate = CurrencyExchangeRates.objects.filter(base=base,target=target).order_by('-fetch_date').first()

        if latest_rate:
            serializer = Currencies_Exchange_Serializer(latest_rate)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No data found'}, status=404)
        
class Currencies(APIView):
    def get(self, request):
        # Filter and get the latest record
        currencies_base = CurrencyExchangeRates.objects.values_list('base',flat=True).distinct()
        currencies_target = CurrencyExchangeRates.objects.values_list('target',flat=True).distinct()
        currencies=list(currencies_base)
        currencies.extend(list(currencies_target))
        currencies=list(set(currencies))
        currencies.sort()
        result = [{"code": currency} for currency in currencies]
        if currencies_base and currencies_base:
            return Response(result,status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No data found'}, status=404)
    

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CurrencyExchangeRates, Currency
from .serializers import Currencies_Serializer,Currencies_Exchange_Serializer
from rest_framework import status

class Get_Exchange_Rates(APIView):
    def get(self, request, base, target):
        
        latest_rate = CurrencyExchangeRates.objects.filter(base=Currency.objects.get(code=base),target=Currency.objects.get(code=target)).order_by('-fetch_date').first()

        if latest_rate:
            serializer = Currencies_Exchange_Serializer(latest_rate)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No data found'}, status=404)
        
class Currencies(APIView):
    def get(self, request):
      
        currencies=Currency.objects.all()
        if currencies:
            serializer=Currencies_Serializer(currencies,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No data found'}, status=404)
    

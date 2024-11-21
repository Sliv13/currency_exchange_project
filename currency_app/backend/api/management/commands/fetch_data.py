from django.core.management.base import BaseCommand
from api.models import CurrencyExchangeRates, User
from rest_framework.response import Response
from rest_framework import status
import yfinance as yf
import os
from dotenv import load_dotenv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--testing', type=bool,default=False)
        parser.add_argument('--base', type=str,default='')
        parser.add_argument('--target', type=str,default='')
        parser.add_argument('--rate', type=float,default=0.0)
        
    def handle(self,*args, **kwargs):
        # get or create superuser
        load_dotenv()
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password=os.getenv('ADMIN_PASSWORD'))
        base_currencies=("EUR","USD","PLN","PLN")
        target_currencies=("USD","JPY","USD","CHF")
        for base_currency,target_currency in zip(base_currencies,target_currencies):
                if base_currency == target_currency:
                    continue
                # Fetch live exchange rate from yfinance
                ticker = f"{base_currency}{target_currency}=X"
                data = yf.Ticker(ticker)
                price = data.history(period="1d").iloc[-1]["Close"]

                # Save to database
                CurrencyExchangeRates.objects.create(
                    base=base_currency,
                    target=target_currency,
                    exchange_rate=price,
                )
                if kwargs['testing']:
                    CurrencyExchangeRates.objects.create(
                    base=kwargs['base'],
                    target=kwargs['target'],
                    exchange_rate=kwargs['rate'],
                )
                    
          

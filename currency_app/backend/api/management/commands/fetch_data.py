from django.core.management.base import BaseCommand
from api.models import CurrencyExchangeRates, User
from rest_framework.response import Response
from rest_framework import status
import yfinance as yf
import os
from dotenv import load_dotenv

class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        # get or create superuser
        load_dotenv()
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password=os.getenv('ADMIN_PASSWORD'))
        base_currencies=("EUR","USD","PLN")
        target_currencies=("USD","JPY","USD")
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
          
        # create CurrencyExchangeRatess - name, desc, price, stock, image

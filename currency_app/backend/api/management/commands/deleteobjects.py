from django.core.management.base import BaseCommand
from api.models import CurrencyExchangeRates


class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        # get or create superuser
        

                # Save to database
                CurrencyExchangeRates.objects.all().delete()
          
        # create CurrencyExchangeRatess - name, desc, price, stock, image

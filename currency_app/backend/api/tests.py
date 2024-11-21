from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command

class CurrenciesTestCase(TestCase):
    def setUp(self) -> None:
        call_command('fetch_data')
        
    def test_currencies_endpoint_status_code(self):
        url=reverse('Currencies')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        
    def test_currencies_endpoint_data(self):
        expected_data=[{'code': 'CHF'}, {'code': 'EUR'}, {'code': 'JPY'}, {'code': 'PLN'}, {'code': 'USD'}]
        url=reverse('Currencies')
        response=self.client.get(url)
        
        self.assertJSONEqual(response.content, expected_data)
        
        
class RatesTestCase(TestCase):
    def setUp(self) -> None:
        call_command('fetch_data','--testing',True,'--base','PLN','--target','USD','--rate', 0.2)
        
    def test_rates_endpoint_status_code(self):
        url=reverse('get_rates', kwargs={'base': 'PLN', 'target': 'USD'})
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        
    def test_rate_endpoint_data(self):
        expected_data={'currency_pair': 'PLNUSD', 'exchange_rate': 0.2}
        url=reverse('get_rates', kwargs={'base': 'PLN', 'target': 'USD'})
        response=self.client.get(url)
        
        self.assertJSONEqual(response.content, expected_data)
        
        
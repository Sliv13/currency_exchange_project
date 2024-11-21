from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command
# Create your tests here.
class CurrenciesTestCase(TestCase):
    def setUp(self) -> None:
        call_command('fetch_data')
        
    def test_endpoint_status_code(self):
        url=reverse('Currencies')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        
    def test_endpoint_data(self):
        expected_data=[{'code': 'CHF'}, {'code': 'EUR'}, {'code': 'JPY'}, {'code': 'PLN'}, {'code': 'USD'}]
        url=reverse('Currencies')
        response=self.client.get(url)
        
        self.assertJSONEqual(response.content, expected_data)
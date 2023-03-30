from django.test import TestCase
from .views import temp
from ShopFinder.settings import BASE_URL
import requests
import json

# Create your tests here.
class ModelTestCase(TestCase):
    def test(self):
        response = requests.get(BASE_URL+"ShopApi/isActive") 
        print(response)
        self.assertEqual(response.status_code,200)

        




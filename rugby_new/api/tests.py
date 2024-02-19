import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import API_formation, API_date
import json

factory = APIRequestFactory()
request = factory.get('formation/')
view = API_formation.as_view()
response = view(request, postal_code='63000')
response.render()
json_response = json.loads(response.content)


class Test_Cities(TestCase):

    def setUp(self):
        pass

    def test_city(self):
        record = {
            "data": [
                {
                    "postal_code": "63000",
                    "name": "clermont",
                    "departement": "puy de dome",
                    "region": "auvergne",
                    "country": "France"
                }
            ]
        }

        self.assertEqual(json_response, record)




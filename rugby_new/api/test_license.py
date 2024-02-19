import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import API_formation, API_date, API_f_license
import json



class test_license(TestCase):
    def setUp(self):
        pass


    def test_license_getPK(self):
        factory = APIRequestFactory()
        request = factory.get('dwh/f_license/')
        view = API_f_license.as_view()
        response = view(request, license_PK='d_federation object (101)f1_4d_geo object (1001CSZ)')
        response.render()
        json_response = json.loads(response.content)

        record = {
            "data": [
                {
                    "license_PK": "d_federation object (101)f1_4d_geo object (1001CSZ)",
                    "count": 0,
                    "federation_FK": "101",
                    "sex_FK": "f",
                    "age_FK": "1_4",
                    "geo_FK": "1001CSZ"
                }
            ]
        }
        print(json_response)
        self.assertEqual(json_response.get('data'), record.get('data'))


    def test_license_getnb_line(self):
        factory = APIRequestFactory()
        request = factory.get('dwh/f_license/')
        view = API_f_license.as_view()
        response = view(request, license_PK='d_federation object (101)f1_4d_geo object (1001CSZ)')
        response.render()
        json_response = json.loads(response.content)

        record = {
            'count': 1
        }
        self.assertEqual(json_response.get('count'), record.get('count'))
    #
    #
    def test_license_get_count(self):
        factory = APIRequestFactory()
        request = factory.get('dwh/f_license/')
        view = API_f_license.as_view()
        response = view(request,  license_PK='d_federation object (101)f1_4d_geo object (1001CSZ)')
        response.render()
        json_response = json.loads(response.content)

        self.assertEqual(json_response['data'][0]['count'], 0)

    #
    def test_license_get_status(self):
            factory = APIRequestFactory()
            request = factory.get('dwh/f_license/')
            view = API_f_license.as_view()
            response = view(request, license_PK='d_federation object (101)f1_4d_geo object (1001CSZ)')
            response.render()

            self.assertEqual(response.status_code, 200)

    def test_date_post_success_status(self):
            factory = APIRequestFactory()
            request = factory.post('formation_date/', data = '')
            view = API_date.as_view()
            response = view(request, )
            response.render()

            self.assertEqual(response.status_code, 201)
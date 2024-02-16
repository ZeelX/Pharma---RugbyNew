from django.shortcuts import render
import json
import sqlite3

from app.models import f_club, f_license
from app.models import d_date, d_age, d_sex, d_geo, d_club_type, d_federation
from api.serializers import f_license_Serializer, f_club_Serializer
from api.serializers import (d_federation_Serializer,
                             d_club_type_Serializer,
                             d_date_Serializer,
                             d_age_Serializer,
                             d_sex_Serializer,
                             d_geo_Serializer,
                             d_club_type_Serializer)

from rugby_new.settings import DATABASES

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DWH_api(APIView):
    """My first API

    Args:
        APIView (_type_): _description_
    """

    def get(self, request, pk=None):

        if 'table' in request.GET:
            table_name = request.GET['table']
            data = eval(table_name).objects.all()
            count = data.count()
        else:
            table_name = 'f_club'
            data = f_club.objects.all()
            count = data.count()

        serializer = eval(f"{table_name}_Serializer")(data=data, many=True)
        serializer.is_valid()

        data = serializer.data

        result = {
            'table_name': table_name,
            'Nombre de ligne': count,
            'data': data
        }

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        result = {
            'message': 'Voici les résultats trouvés',
            'data': []
        }

        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        result = {
            'message': 'Voici les résultats trouvés',
            'data': []
        }

        return Response(result, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        result = {
            'message': 'Voici les résultats trouvés',
            'data': []
        }

        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):



        rows = d_geo.objects.all()
        count = rows.count()
        rows.delete()

        rows = d_age.objects.all()
        count = rows.count()
        rows.delete()

        rows = d_federation.objects.all()
        count = rows.count()
        rows.delete()

        rows = d_club_type.objects.all()
        count = rows.count()
        rows.delete()

        rows = d_sex.objects.all()
        count = rows.count()
        rows.delete()

        rows = d_date.objects.all()
        count = rows.count()
        rows.delete()

        rows = f_license.objects.all()
        count = rows.count()
        rows.delete()

        conn = sqlite3.connect(DATABASES['default']['NAME'])
        conn.execute("VACUUM")
        conn.close()

        result = {
            'message': f"{count} lignes ont été supprimées",
            'data': []
        }

        return Response(result, status=status.HTTP_200_OK)
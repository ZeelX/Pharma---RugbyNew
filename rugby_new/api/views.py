from django.shortcuts import render
import json
import sqlite3

from rest_framework.pagination import PageNumberPagination

from app.models import f_club, f_license
from app.models import d_date, d_age, d_sex, d_geo, d_club_type, d_federation, city
from api.serializers import f_license_Serializer, f_club_Serializer, city_Serializer
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

    def get(self, request, PK=None):

        if 'table' in request.GET:
            table_name = request.GET['table']
            data = eval(table_name).objects.all()
            count = data.count()
        else:
            table_name = 'f_club'
            data = f_club.objects.all()
            count = data.count()

        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_queryset = paginator.paginate_queryset(data, request)

        serializer = eval(f"{table_name}_Serializer")(data=paginated_queryset, many=True)
        serializer.is_valid()

        data = serializer.data

        result = {
            'home': 'http://localhost:8000/',
            'table_name': table_name,
            'Nombre de ligne': count,
            'data': data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):

        pass
        # data = request.data
        # serializer = d_date_Serializer(data=data)
        #
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    # def delete(self, request, pk=None):
    #
    #     rows = d_geo.objects.all()
    #     count = rows.count()
    #     rows.delete()
    #
    #     rows = d_age.objects.all()
    #     count = rows.count()
    #     rows.delete()
    #
    #     rows = d_federation.objects.all()
    #     count = rows.count()
    #     rows.delete()
    #
    #     rows = d_club_type.objects.all()
    #     count = rows.count()
    #     rows.delete()
    #
    #     rows = d_sex.objects.all()
    #     count = rows.count()
    #     rows.delete()
    #
    #     rows = d_date.objects.all()
    #     count = rows.count()
    #     rows.delete()
    #
    #     rows = f_license.objects.all()
    #     count = rows.count()
    #     rows.delete()
    #
    #     conn = sqlite3.connect(DATABASES['default']['NAME'])
    #     conn.execute("VACUUM")
    #     conn.close()
    #
    #     result = {
    #         'message': f"{count} lignes ont été supprimées",
    #         'data': []
    #     }

        return Response(result, status=status.HTTP_200_OK)
class API_f_license(APIView):
    lookup_field = 'license_PK'

    def get(self, request, license_PK=None):

        if license_PK is not None:
            data = f_license.objects.filter(license_PK=license_PK)
            serializer = f_license_Serializer(data=data, many=True)

        else:
            data = f_license.objects.all()
            serializer = f_license_Serializer(data=data, many=True)

        serializer.is_valid()

        result = {
            'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)



class API_date(APIView):
    lookup_field = 'date_PK'

    def get(self, request, date_PK=None):

        if date_PK is not None:
            data = d_date.objects.filter(date_PK=date_PK)
            serializer = d_date_Serializer(data=data, many=True)

        else:
            data = d_date.objects.all()
            serializer = d_date_Serializer(data=data, many=True)

        serializer.is_valid()

        result = {
            # 'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = d_date_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class API_formation(APIView):
    """

    """
    lookup_field = 'postal_code'
    def get(self, request, postal_code=None):

        if postal_code is not None:
            data = city.objects.filter(postal_code=postal_code)
            serializer = city_Serializer(data=data, many=True)

        else:
            data = city.objects.all()
            serializer = city_Serializer(data=data, many=True)

        serializer.is_valid()

        result = {
            # 'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = city_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

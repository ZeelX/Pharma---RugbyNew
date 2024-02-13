# from django.shortcuts import render
# from app.models import ODS
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
#
#
# class EndPointDWH(APIView):
#     """My frist API
#
#     Args:
#         APIView (_type_): _description_
#     """
#
#     def get(self, request, format=None):
#         table = request.GET['table']
#
#         result = {
#             'message': 'Résultat de ma table de fait',
#             'Nombre de ligne': 540,
#             'nom de table': table
#         }
#
#         return Response(result)
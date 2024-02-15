# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')
#
# # Chargez la configuration de Django
# django.setup()
#
# from app.models import ODS, ODS_License, d_geo
# from django.db.models import Q
#
#
# def extract_data_ods_clubs():
#     return ODS.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))
#
#
# def extract_data_ods_license():
#     return ODS_License.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))
#
#
# d_geo.objects.all().delete()
# geo_list = []
#
# for data in extract_data_ods_clubs():
#     geo_key_check = data.code_commune + data.code_qpv
#     if not any(element.geo_key == geo_key_check for element in geo_list):
#         geo_instance = d_geo(
#             geo_key=geo_key_check,
#             code_commune=data.code_commune,
#             label_commune=data.commune,
#             code_qpv=data.code_qpv,
#             label_aqpv=data.nom_qpv,
#             code_departement=data.departement,
#             label_departement="",
#             region=data.region,
#             statut_geo=data.statut_geo,
#         )
#         geo_list.append(geo_instance)
#     else:
#         continue
#
# d_geo.objects.bulk_create(geo_list)
#
# geo_list.clear()
# existing_keys = set(element.geo_key for element in geo_list)
#
# for data in extract_data_ods_license():
#     geo_key_check = data.code_commune + data.code_QPV
#     if geo_key_check not in existing_keys:
#         # Vérifier en base de données
#         if not d_geo.objects.filter(geo_key=geo_key_check).exists():
#             obj, created = d_geo.objects.get_or_create(
#                 geo_key=geo_key_check,
#                 defaults={
#                     'geo_key': geo_key_check,
#                     'code_commune': data.code_commune,
#                     'label_commune': data.commune,
#                     'code_qpv': data.code_QPV,
#                     'label_qpv': data.name_qpv,
#                     'code_departement': data.departement,
#                     'label_departement': "",
#                     'region': data.region,
#                     'statut_geo': data.statut_geo,
#                 }
#             )
#             if created:
#                 geo_list.append(obj)
#             existing_keys.add(geo_key_check)
# d_geo.objects.bulk_create(geo_list)


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from app.models import ODS, ODS_License, d_geo
from django.db.models import Q


def extract_data_ods_clubs():
    return ODS.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


def extract_data_ods_license():
    return ODS_License.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


d_geo.objects.all().delete()
geo_list = []
existing_keys = set()

# Première boucle pour extraire les données d'ODS clubs
for data in extract_data_ods_clubs():
    geo_key_check = data.code_commune + data.code_qpv
    if geo_key_check not in existing_keys:
        geo_instance = d_geo(
            geo_key=geo_key_check,
            code_commune=data.code_commune,
            label_commune=data.commune,
            code_qpv=data.code_qpv,
            label_qpv=data.nom_qpv,
            code_departement=data.departement,
            label_departement="",
            region=data.region,
            statut_geo=data.statut_geo,
        )
        geo_list.append(geo_instance)
        existing_keys.add(geo_key_check)

d_geo.objects.bulk_create(geo_list)
geo_list.clear()

# Deuxième boucle pour extraire les données d'ODS license
for data_license in extract_data_ods_license():
    geo_key_check = data_license.code_commune + data_license.code_QPV
    if geo_key_check not in existing_keys:
        # Vérifier en base de données
        geo_instance = d_geo(
            geo_key=geo_key_check,
            code_commune=data_license.code_commune,
            label_commune=data_license.commune,
            code_qpv=data_license.code_QPV,
            label_qpv=data_license.name_qpv,
            code_departement=data_license.departement,
            label_departement="",
            region=data_license.region,
            statut_geo=data_license.statut_geo,
            )

        geo_list.append(geo_instance)
        existing_keys.add(geo_key_check)

d_geo.objects.bulk_create(geo_list)


import os
import django
import sqlite3
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from app.models import ODS, d_geo
from django.db.models import Q


def extract_data_ods_clubs():
    return ODS.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


def extract_data_ods_license():

    df2 = pd.read_sql_query("SELECT * FROM app_ods_license WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", sqlite3.connect('../db.sqlite3'))

    df2 = df2.loc[:, ~df2.columns.str.contains('f_nr|h_nr|nr_nr')]
    return df2


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
for _, row in extract_data_ods_license().iterrows():
    geo_key_check = row['code_commune'] + row['code_QPV']
    if geo_key_check not in existing_keys:
        # Vérifier en base de données
        geo_instance = d_geo(
            geo_key=geo_key_check,
            code_commune=row['code_commune'],
            label_commune=row['commune'],
            code_qpv=row['code_QPV'],
            label_qpv=row['name_qpv'],
            code_departement=row['departement'],
            label_departement="",
            region=row['region'],
            statut_geo=row['statut_geo'],
            )

        geo_list.append(geo_instance)
        existing_keys.add(geo_key_check)

d_geo.objects.bulk_create(geo_list)


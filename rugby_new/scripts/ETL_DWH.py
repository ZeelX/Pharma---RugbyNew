import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from app.models import ODS, d_club_type, d_geo, d_federation
from django.db.models import Q


# TODO => recupérer les datas


def extract_data_ods_clubs():
    return ODS.objects.filter(~Q(code_commune='NR - Non réparti'))


d_geo.objects.all().delete()
d_federation.objects.all().delete()
d_club_type.objects.all().delete()

ods_club = extract_data_ods_clubs()

geo_list = []
federation_list = []
club_list = []

for data in ods_club:
    geo_key_check = data.code_commune + data.code_qpv
    if not any(element.geo_key == geo_key_check for element in geo_list):
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
    else:
        continue

    if not any(element.code_federation == data.code for element in federation_list):
        federation_instance = d_federation(
                    code_federation=data.code,
                    label=data.federation,
                )
        federation_list.append(federation_instance)
    else:
        continue
    if not any(element.code_club_type == data.clubs for element in club_list):

        club_instance = d_club_type(
                    code_club_type=data.clubs
                )
        club_list.append(club_instance)
    else:
        continue

d_geo.objects.bulk_create(geo_list)
d_federation.objects.bulk_create(federation_list)
d_club_type.objects.bulk_create(club_list)

# TODO => Trier les datas selon les colonnes des tables


# TODO => Faire le push des données

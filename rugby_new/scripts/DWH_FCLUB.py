import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from app.models import ODS, d_club_type, d_federation, d_date, d_geo, f_club
from django.db.models import Q


def extract_data_ods_clubs():
    return ODS.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


f_club.objects.all().delete()
f_club_list = []
existing_keys = set()

# Première boucle pour extraire les données d'ODS clubs
for data in extract_data_ods_clubs():
    f_club_key_check = data.epa + data.code + '2021-01-01' + data.code_commune + data.code_qpv
    if f_club_key_check not in existing_keys:
        # Récupérer les instances des clés étrangères
        club_type_instance, created = d_club_type.objects.get_or_create(code_club_type=data.epa)
        federation_instance, created = d_federation.objects.get_or_create(code_federation=data.code)
        date_instance, created = d_date.objects.get_or_create(date_PK='2021-01-01')
        geo_instance, created = d_geo.objects.get_or_create(geo_key=data.code_commune + data.code_qpv)
        # Créer l'instance de f_club avec les clés étrangères récupérées
        federation_instance = f_club(
            club_PK=f_club_key_check,
            club_type_FK=club_type_instance,
            federation_FK=federation_instance,
            date_FK=date_instance,
            geo_FK=geo_instance,
            count=data.clubs,
        )
        f_club_list.append(federation_instance)
        existing_keys.add(f_club_key_check)

f_club.objects.bulk_create(f_club_list)

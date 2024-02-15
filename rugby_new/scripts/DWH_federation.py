import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from app.models import ODS, ODS_License, d_federation
from django.db.models import Q


def extract_data_ods_clubs():
    return ODS.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


def extract_data_ods_license():
    return ODS_License.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


d_federation.objects.all().delete()
federation_list = []
existing_keys = set()

# Première boucle pour extraire les données d'ODS clubs
for data in extract_data_ods_clubs():
    fede_key_check = data.code
    if fede_key_check not in existing_keys:
        federation_instance = d_federation(
            code_federation=data.code,
            label=data.federation
        )
        federation_list.append(federation_instance)
        existing_keys.add(fede_key_check)

d_federation.objects.bulk_create(federation_list)
federation_list.clear()

# Deuxième boucle pour extraire les données d'ODS license
for data_license in extract_data_ods_license():
    fede_key_check = data_license.code
    if fede_key_check not in existing_keys:
        federation_instance = d_federation(
            code_federation=data_license.code,
            label=data_license.fede
        )
        federation_list.append(federation_instance)
        existing_keys.add(fede_key_check)

d_federation.objects.bulk_create(federation_list)



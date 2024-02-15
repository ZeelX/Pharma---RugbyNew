import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

django.setup()

from app.models import ODS, ODS_License, d_club_type
from django.db.models import Q


def extract_data_ods_clubs():
    return ODS.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


def extract_data_ods_license():
    return ODS_License.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))

d_club_type.objects.all().delete()
club_list = []
existing_keys = set()

for data in extract_data_ods_clubs():
    club_key_check = data.epa
    if club_key_check not in existing_keys:
        club_instance = d_club_type(
            code_club_type=data.epa
        )
        club_list.append(club_instance)
        existing_keys.add(club_key_check)

d_club_type.objects.bulk_create(club_list)




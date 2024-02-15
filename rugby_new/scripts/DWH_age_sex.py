import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

django.setup()

from app.models import ODS, ODS_License, d_age, d_sex
from django.db.models import Q


def extract_data_ods_license():
    return ODS_License.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


d_age.objects.all().delete()
d_sex.objects.all().delete()
age_set = set()
age_list = []

for element in extract_data_ods_license():
    for attr_name, attr_value in element.__dict__.items():
        if (attr_name.startswith('h') or attr_name.startswith('f')) and attr_name != 'fede' and attr_name != 'f_nr' and attr_name != 'h_nr':
            age = attr_name[1:]
            age_set.add(age)

for element in age_set:
    age_instance = d_age(
        code_age=element
    )
    age_list.append(age_instance)

d_age.objects.bulk_create(age_list)

sex_value = ['h', 'f']
for value in sex_value:
    instance = d_sex(code_sex=value)
    instance.save()

import os
import django
import re
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from app.models import ODS_License, d_federation, d_sex, d_age, d_date, d_geo, f_license
from django.db.models import Q


def extract_data_f_license():
    return ODS_License.objects.filter(~Q(code_commune='NR - Non réparti'), Q(region='Auvergne-Rhône-Alpes'))


f_license.objects.all().delete()
f_license_list = []

def extract_code_sex_and_age(element):
    for attr_name, attr_value in element.__dict__.items():
        if (attr_name.startswith('h') or attr_name.startswith('f')) and attr_name != 'fede' and attr_value != '0':
            sex = attr_name[0]
            age = attr_name[1:]
            count = attr_value
            return sex, age, count




for data in extract_data_f_license():
    extraction = extract_code_sex_and_age(data)
    print(extraction)
    federation_instance, _ = d_federation.objects.get_or_create(code_federation=data.fede)
    sex_instance, _ = d_sex.objects.get_or_create(code_sex=extraction[0])
    age_instance, _ = d_age.objects.get_or_create(code_age=extraction[1])
    date_instance, _ = d_date.objects.get_or_create(date_PK='2021-01-01')
    geo_instance, _ = d_geo.objects.get_or_create(
        geo_key=data.code_commune + data.code_QPV,
        code_commune=data.code_commune,
        label_commune=data.commune,
        code_qpv=data.code_QPV,
        label_qpv=data.name_qpv,
        code_departement=data.departement,
        label_departement='',
        region=data.region,
        statut_geo=data.statut_geo
    )

    # Créer l'instance f_license
    f_license_instance = f_license(
        license_PK=data.fede + extraction[0] + extraction[1] + '2021-01-01' + data.code_commune + data.code_QPV,
        federation_FK=federation_instance,
        sex_FK=sex_instance,
        age_FK=age_instance,
        date_FK=date_instance,
        geo_FK=geo_instance,
        count=extraction[2]
    )
    f_license_list.append(f_license_instance)

f_license.objects.bulk_create(f_license_list)

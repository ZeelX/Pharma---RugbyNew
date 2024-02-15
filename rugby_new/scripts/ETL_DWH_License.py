import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

# Chargez la configuration de Django
django.setup()

from app.models import ODS_License, d_club_type, d_age, d_geo, d_sex, d_date, d_federation, f_club, f_license
from django.db.models import Q


def extract_data_ods_license():
    return ODS_License.objects.filter(~Q(code_commune='NR - Non réparti'))


d_geo.objects.all().delete()
d_age.objects.all().delete()
d_sex.objects.all().delete()
d_date.objects.all().delete()
d_federation.objects.all().delete()

geo_list = []

for data in extract_data_ods_license():
    geo_key_check = data.code_commune + data.code_QPV
    obj, created = d_geo.objects.get_or_create(

         geo_key=geo_key_check,
         code_commune=data.code_commune,
         label_commune=data.commune,
         code_qpv=data.code_QPV,
         label_qpv=data.name_qpv,
         code_departement=data.departement,
         label_departement="",
         region=data.region,
         statut_geo=data.statut_geo,
                )
    if created:
        geo_list.append(obj)


print(geo_list)
            # code
            # fede
            # f1_4
            # f5_9
            # f10_14
            # f15_19
            # f20_24
            # f25_29=row['F - 25 à 29 ans'],
            # f30_34=row['F - 30 à 34 ans'],
            # f35_39=row['F - 35 à 39 ans'],
            # f40_44=row['F - 40 à 44 ans'],
            # f45_49=row['F - 45 à 49 ans'],
            # f50_54=row['F - 50 à 54 ans'],
            # f55_59=row['F - 55 à 59 ans'],
            # f60_64=row['F - 60 à 64 ans'],
            # f64_69=row['F - 65 à 69 ans'],
            # f70_74=row['F - 70 à 74 ans'],
            # f75_79=row['F - 75 à 79 ans'],
            # f80_99=row['F - 80 à 99 ans'],
            # f_nr=row['F - NR'],
            # h1_4=row['H - 1 à 4 ans'],
            # h5_9=row['H - 5 à 9 ans'],
            # h10_14=row['H - 10 à 14 ans'],
            # h15_19=row['H - 15 à 19 ans'],
            # h20_24=row['H - 20 à 24 ans'],
            # h25_29=row['H - 25 à 29 ans'],
            # h30_34=row['H - 30 à 34 ans'],
            # h35_39=row['H - 35 à 39 ans'],
            # h40_44=row['H - 40 à 44 ans'],
            # h45_49=row['H - 45 à 49 ans'],
            # h50_54=row['H - 50 à 54 ans'],
            # h55_59=row['H - 55 à 59 ans'],
            # h60_64=row['H - 60 à 64 ans'],
            # h64_69=row['H - 65 à 69 ans'],
            # h70_74=row['H - 70 à 74 ans'],
            # h75_79=row['H - 75 à 79 ans'],
            # h80_99=row['H - 80 à 99 ans'],
            # h_nr=row['H - NR'],
            # NRNR=row['NR - NR'],
            # total=row['Total'],

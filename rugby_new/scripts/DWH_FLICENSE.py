import os
import django
import sqlite3
import pandas as pd
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')
django.setup()

from app.models import d_federation, d_sex, d_age, d_geo, f_license

conn = sqlite3.connect('../db.sqlite3')

df_app_club_2 = pd.read_sql_query(
    "SELECT * FROM app_ods_license WHERE region = 'Auvergne-Rhône-Alpes' AND code_commune != 'NR - Non réparti'", conn)
df_app_club_2 = df_app_club_2.loc[:, ~df_app_club_2.columns.str.contains('f_nr|h_nr|nr_nr')]

sex_dict = {sex.code_sex: sex for sex in d_sex.objects.all()}
age_dict = {age.code_age: age for age in d_age.objects.all()}
fede_dict = {fede.code_federation: fede for fede in d_federation.objects.all()}
local_dict = {local.geo_key: local for local in d_geo.objects.all()}
licences_to_create = []
start_time = time.time()

print('start ODS_license')
for _, row in df_app_club_2.iterrows():
    for col in row.index:
        if col.startswith(('f', 'h')) and not col.startswith(('fede')):
            sex_code = col[0]
            sex = sex_dict.get(sex_code)
            age_label = col[1:]
            age = age_dict.get(age_label)
            if sex and age:

                code_federation = row['code']
                fede = fede_dict.get(code_federation)
                local_id = row['code_commune'] + row['code_QPV']
                local = local_dict.get(local_id)
                if fede and local:

                    nb_target = row[col]
                    print(nb_target)
                    if nb_target is not None:
                        licence = f_license(
                            license_PK=str(fede) + sex_code + age_label + str(local),
                            federation_FK=fede,
                            sex_FK=sex,
                            age_FK=age,
                            geo_FK=local,
                            count=nb_target
                        )
                        licences_to_create.append(licence)
                    else:
                        print("Erreur: Valeur NULL détectée pour le nombre cible")
                else:
                    print("Erreur: Fédération ou Localisation non trouvée pour :", fede, local_id)

f_license.objects.bulk_create(licences_to_create)

end_time = time.time()
execution_time = end_time - start_time
print(f"Temps d'exécution: {execution_time} secondes")
conn.close()

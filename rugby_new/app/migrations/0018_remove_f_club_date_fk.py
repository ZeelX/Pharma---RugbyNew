# Generated by Django 5.0.2 on 2024-02-19 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_f_license_date_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f_club',
            name='date_FK',
        ),
    ]

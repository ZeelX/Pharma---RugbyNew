# Generated by Django 5.0.2 on 2024-02-13 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_ods_license_code_qpv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ods_license',
            old_name='Total',
            new_name='total',
        ),
    ]

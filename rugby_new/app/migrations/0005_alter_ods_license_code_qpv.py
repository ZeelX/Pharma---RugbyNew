# Generated by Django 5.0.2 on 2024-02-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ods_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ods_license',
            name='code_QPV',
            field=models.CharField(max_length=500),
        ),
    ]
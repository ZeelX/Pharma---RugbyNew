# Generated by Django 5.0.2 on 2024-02-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_d_date_date_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d_date',
            name='date_PK',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_d_date_date_pk'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('postal_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('departement', models.CharField(max_length=150)),
                ('region', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
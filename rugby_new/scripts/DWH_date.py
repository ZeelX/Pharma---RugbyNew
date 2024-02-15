import os
from datetime import date
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rugby_new.settings')

django.setup()

from app.models import d_date

d_date.objects.all().delete()


d_date_instance = d_date(date_PK=date(2021, 1, 1))
d_date_instance.save()

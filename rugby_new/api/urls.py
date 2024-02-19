from django.urls import path
from api.views import DWH_api, API_formation, API_date, API_f_license

urlpatterns = [
    path('dwh/f_license/<license_PK>', API_f_license.as_view()),
    path('formation_date/<date_PK>', API_date.as_view()),
    path('formation/<postal_code>/', API_formation.as_view()),

    path('dwh/f_license', API_f_license.as_view()),
    path('formation/', API_formation.as_view()),
    path('formation_date/', API_date.as_view()),

    path('dwh/', DWH_api.as_view()),

]


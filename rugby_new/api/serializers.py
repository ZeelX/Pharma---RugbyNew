from rest_framework import serializers
from app.models import (f_club,
                        f_license,
                        d_date,
                        d_age,
                        d_sex,
                        d_geo,
                        d_club_type,
                        d_federation)


class f_club_Serializer(serializers.ModelSerializer):
    class Meta:
        model = f_club
        fields = '__all__'


class f_license_Serializer(serializers.ModelSerializer):
    class Meta:
        model = f_license
        fields = '__all__'


class d_date_Serializer(serializers.ModelSerializer):
    class Meta:
        model = d_date
        fields = '__all__'


class d_age_Serializer(serializers.ModelSerializer):
    class Meta:
        model = d_age
        fields = '__all__'


class d_sex_Serializer(serializers.ModelSerializer):
    class Meta:
        model = d_sex
        fields = '__all__'


class d_geo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = d_geo
        fields = '__all__'


class d_club_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = d_club_type
        fields = '__all__'


class d_federation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = d_federation
        fields = '__all__'

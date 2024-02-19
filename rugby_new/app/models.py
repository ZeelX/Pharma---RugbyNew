from django.db import models

# Create your models here.

class Player(models.Model):
    """

    _summary_
    :arg
    """


    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self,):
        return f"{self.first_name} - {self.last_name}"


class ODS(models.Model):
    

    
    code_commune = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    code_qpv = models.CharField(max_length=255)
    nom_qpv = models.CharField(max_length=255)
    departement = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    federation = models.CharField(max_length=255)
    clubs = models.CharField(max_length=255)
    epa = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)




class ODS_License(models.Model):
    code_commune = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    code_QPV = models.CharField(max_length=500)
    name_qpv = models.CharField(max_length=255)
    departement = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    fede = models.CharField(max_length=255)
    f1_4 = models.CharField(max_length=255)
    f5_9 = models.CharField(max_length=255)
    f10_14 = models.CharField(max_length=255)
    f15_19 = models.CharField(max_length=255)
    f20_24 = models.CharField(max_length=255)
    f25_29 = models.CharField(max_length=255)
    f30_34 = models.CharField(max_length=255)
    f35_39 = models.CharField(max_length=255)
    f40_44 = models.CharField(max_length=255)
    f45_49 = models.CharField(max_length=255)
    f50_54 = models.CharField(max_length=255)
    f55_59 = models.CharField(max_length=255)
    f60_64 = models.CharField(max_length=255)
    f64_69 = models.CharField(max_length=255)
    f70_74 = models.CharField(max_length=255)
    f75_79 = models.CharField(max_length=255)
    f80_99 = models.CharField(max_length=255)
    f_nr = models.CharField(max_length=255)
    h1_4 = models.CharField(max_length=255)
    h5_9 = models.CharField(max_length=255)
    h10_14 = models.CharField(max_length=255)
    h15_19 = models.CharField(max_length=255)
    h20_24 = models.CharField(max_length=255)
    h25_29 = models.CharField(max_length=255)
    h30_34 = models.CharField(max_length=255)
    h35_39 = models.CharField(max_length=255)
    h40_44 = models.CharField(max_length=255)
    h45_49 = models.CharField(max_length=255)
    h50_54 = models.CharField(max_length=255)
    h55_59 = models.CharField(max_length=255)
    h60_64 = models.CharField(max_length=255)
    h64_69 = models.CharField(max_length=255)
    h70_74 = models.CharField(max_length=255)
    h75_79 = models.CharField(max_length=255)
    h80_99 = models.CharField(max_length=255)
    h_nr = models.CharField(max_length=255)
    NRNR = models.CharField(max_length=255)
    total = models.CharField(max_length=255)


class d_sex(models.Model):
    code_sex = models.CharField(max_length=2, primary_key=True,unique=True)

class d_age(models.Model):
    code_age = models.CharField(max_length=10, primary_key=True,unique=True)

class d_club_type(models.Model):
    code_club_type = models.CharField(max_length=50, primary_key=True,unique=True)

class d_federation(models.Model):
    code_federation = models.CharField(max_length=15, primary_key=True,unique=True)
    label = models.CharField(max_length=100)

class d_date(models.Model):
    date_PK = models.DateField(primary_key=True)

class d_geo(models.Model):
    geo_key = models.CharField(max_length=250, default=None, primary_key= True, unique=True)
    code_commune = models.CharField(max_length=150)
    label_commune = models.CharField(max_length=150)
    code_qpv = models.CharField(max_length=150)
    label_qpv = models.CharField(max_length=150)
    code_departement = models.CharField(max_length=150)
    label_departement = models.CharField(max_length=150)
    region = models.CharField(max_length=150)
    statut_geo = models.CharField(max_length=150, default=None)

class f_license(models.Model):
    license_PK = models.CharField(max_length=250, primary_key= True, unique=True)
    federation_FK = models.ForeignKey(d_federation, on_delete=models.CASCADE)
    sex_FK = models.ForeignKey(d_sex, on_delete=models.CASCADE)
    age_FK = models.ForeignKey(d_age, on_delete=models.CASCADE)
    geo_FK = models.ForeignKey(d_geo, on_delete=models.CASCADE)
    count = models.IntegerField(default = None)
    # pk => federation_FK + sex_FK + age_FK + geo_FK
class f_club(models.Model):
    club_PK = models.CharField(max_length=250, primary_key= True,unique=True)
    club_type_FK = models.ForeignKey(d_club_type, on_delete=models.CASCADE)
    federation_FK = models.ForeignKey(d_federation, on_delete=models.CASCADE)
    geo_FK = models.ForeignKey(d_geo, on_delete=models.CASCADE)
    count = models.IntegerField(default= None)
    #PK => club_type_FK + federation_FK + date_FK+ geo_FK

class city(models.Model):
    postal_code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=300)
    departement = models.CharField(max_length=150)
    region = models.CharField(max_length=150)
    country = models.CharField(max_length=100)



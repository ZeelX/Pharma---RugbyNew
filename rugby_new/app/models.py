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
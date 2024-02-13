# from django.db import models
#
#
# # Create your models here.
# class d_geo(models.Model):
#     departement = models.CharField(max_length=50, primary_key=True)
#     region = models.CharField(max_length=50, primary_key=True)
#     code_commune = models.IntegerField(primary_key=True)
#     label_commune = models.CharField(max_length=75)
#     statut_geo = models.CharField(max_length=20)
#
#     def __str__(self):
#         return f"{self.label_commune} - {self.departement} - {self.region}"
#
# class QPV(models.Model):
#     code_qpv = models.IntegerField(primary_key=True)
#     label_qpv = models.CharField(max_length=25)
#
#     def __str__(self):
#         return f"{self.label_qpv}"
#
# class federation(models.Model):
#     code_fede = models.IntegerField(primary_key=True)
#     label_fede = models.CharField(max_length=150)
#
#     def __str__(self):
#         return f"{self.label_fede}"
#
# class sex(models.Model):
#     code_sex = models.IntegerField(primary_key=True)
#     label_sex = models.CharField(max_length=9)
#
#     def __str__(self):
#         return f"{self.label_sex}"
#
# class age(models.Model):
#     age = models.CharField(max_length=10, primary_key=True)
#
#     def __str__(self):
#         return f"{self.age}"
#
# class license(models.Model):
#     geo_FK = models.ForeignKey(d_geo, on_delete=models.CASCADE, primary_key=True)
#     qpv_FK = models.ForeignKey(QPV, on_delete=models, primary_key=True)
#     federation_FK = models.ForeignKey(federation, on_delete=models, primary_key=True)
#     sex_FK = models.ForeignKey(sex, on_delete=models, primary_key=True)
#     age_fK = models.ForeignKey(age, on_delete=models, primary_key=True)
#     count = models.IntegerField()
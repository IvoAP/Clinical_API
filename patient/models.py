from django.db import models


class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    date_born = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    number_address = models.IntegerField(blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    rg = models.CharField(max_length=100, blank=True, null=True)

    class Meta :
        managed = True
        db_table = 'patients'
    






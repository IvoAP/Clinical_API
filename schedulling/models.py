from django.db import models

from patient.models import Patient


class Schedulling(models.Model):
    id_schedulling = models.AutoField(primary_key=True)
    date_hour = models.DateTimeField(blank=False, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    canceled_schedulling = models.BooleanField(default=False)
    obs = models.TextField(blank=True, null=True) 
    type_schedulling = models.CharField(max_length=100, blank=True, null=True)
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='schedulling', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'schedulling'
        unique_together = ('date_hour', 'id_patient' )

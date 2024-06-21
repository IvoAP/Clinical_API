from rest_framework import viewsets

from patient.api.serializers import PatientSerializer
from patient.models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
from rest_framework import viewsets

from schedulling.api.serializers import SchedullingSerializer
from schedulling.models import Schedulling


class SchedullingViewSet(viewsets.ModelViewSet):
    queryset = Schedulling.objects.all().order_by('date_hour')
    serializer_class = SchedullingSerializer
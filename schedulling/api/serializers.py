from rest_framework import serializers

from schedulling.models import Schedulling


class SchedullingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedulling
        fields = '__all__'

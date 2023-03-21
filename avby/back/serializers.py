from rest_framework import serializers
from back.models import TransportModel, TransportAd, TransportMark


class TransportMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMark
        fields = '__all__'

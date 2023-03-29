from rest_framework import serializers
from back.models import TransportModel, TransportAd, TransportMark


class TransportMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMark
        fields = '__all__'


class TransportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportModel
        fields = '__all__'
        read_only_fields = ['mark',]


class TransportModelCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportModel
        fields = '__all__'
        read_only_fields = ['mark',]

    def validate(self, data):
        data['mark'] = TransportMark.objects.get(pk=self.context['mark'])
        return data


class TransportAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportAd
        fields = '__all__'





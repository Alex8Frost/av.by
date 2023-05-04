from rest_framework import serializers
from back.models import TransportModel, TransportAd, TransportMark
from django.conf import settings


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
        print()
        return data


class TransportAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportAd
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['email', 'password', 'first_name', 'last_name']






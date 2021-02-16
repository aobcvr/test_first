from clients.models import Client
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    gems = serializers.CharField(source='get_gems',)

    class Meta:
        model = Client
        fields = ('username', 'spent_money', 'gems',)

from clients.models import Client
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    gems = serializers.ReadOnlyField(source='get_gems',)

    class Meta:
        model = Client
        fields = ('username', 'spent_money', 'gems',)

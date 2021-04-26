from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    items = serializers.ReadOnlyField(source='get_items', )

    class Meta:
        model = Client
        fields = ('username', 'spent_money', 'items',)

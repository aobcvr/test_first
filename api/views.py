from deals.models import Deal
from clients.models import Client
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ClientSerializer


class DealViewSet(viewsets.ViewSet):
    """
    Get top 5 clients, or update the deals table via .csv file
    """

    @action(detail=False, methods=['get'],)
    def get_top_clients(self, request,):
        serializer = ClientSerializer(Client.get_top_clients(), many=True)
        return Response({'response': serializer.data})

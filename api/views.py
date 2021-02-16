from django.utils.translation import gettext_lazy as _

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.exceptions import ParseError

from .serializers import ClientSerializer
from deals.resources import DealResource
from clients.models import Client


class DealViewSet(viewsets.ViewSet):
    """
    Get top 5 clients, or update the deals table via .csv file
    """

    parser_classes = (MultiPartParser,)

    @action(detail=False, methods=['get'],)
    def list_top_clients(self, request,):
        serializer = ClientSerializer(Client.get_top_clients(), many=True)
        return Response({'response': serializer.data})

    @action(detail=False, methods=['post'])
    def import_deals_file(self, request,):
        if 'file' not in request.data or \
                request.data['file'].name != 'deals.csv':
            raise ParseError(_('Прикрепите файл deals.csv.'))

        data = request.data['file']
        resource = DealResource()
        result = resource.import_file(data, dry_run=True)

        if result.has_errors():
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={
                    'error': _(
                        'В процессе обработки файла произошла ошибка.')
                }
            )
        else:
            result = resource.import_file(data, dry_run=False)
            return Response(status=status.HTTP_200_OK, data={
                'detail': _(
                    'Файл был обработан без ошибок.'
                ),
                'totals': result.totals  # перечень обработанных строк
            })

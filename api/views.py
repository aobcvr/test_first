import logging

import tablib
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from clients.models import Client
from deals.resources import DealResource
from .serializers import ClientSerializer

logger = logging.getLogger(__name__)


class DealViewSet(viewsets.ViewSet):
    """
    Get top 5 clients, or update the deals table via .csv file
    """

    parser_classes = (MultiPartParser,)

    @action(detail=False, methods=["get"], )
    def list_leaderboard(self, request, ):
        serializer = ClientSerializer(Client.get_leaderboard(), many=True)
        return Response({"response": serializer.data})

    @action(detail=False, methods=["post"], )
    def import_deals_file(self, request, ):
        try:
            file = request.data["file"]
            resource = DealResource()
            dataset = tablib.Dataset().load(file.read().decode(), format='csv', )
            result = resource.import_data(dataset, dry_run=False, raise_errors=True, collect_failed_rows=True)
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "detail": _("Файл был обработан без ошибок."),
                    "totals": result.totals,  # перечень обработанных строк
                },
            )
        except MultiValueDictKeyError:
            raise ParseError(_("Прикрепите файл deals.csv."))
        except:
            logger.exception('Failed to import deals file')
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"error": _("В процессе обработки файла произошла неизвестная ошибка.")},
            )

from core.models import Client
from import_export import resources


class ClientResource(resources.ModelResource):

    class Meta:
        model = Client

from import_export import resources, fields

from clients.models import Client
from deals.models import Deal
from items.models import Item


class DealResource(resources.ModelResource):
    total_currency = fields.Field(attribute='total_currency', column_name='total_currency', default="USD",
                                  saves_null_values=False)

    def before_import_row(
        self,
        row,
        **kwargs,
    ):
        client_name = row["customer"]
        item_name = row["item"]

        client, _ = Client.objects.get_or_create(username=client_name)
        item, _ = Item.objects.get_or_create(name=item_name, )

        row["customer"] = client.pk
        row["item"] = item.pk

    class Meta:
        model = Deal
        skip_unchanged = True
        export_order = (
            "customer",
            "item",
            "total",
            "quantity",
            "date",
        )

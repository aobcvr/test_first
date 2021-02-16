import tablib
import io

from import_export import resources

from clients.models import Client
from deals.models import Deal
from items.models import Item


class DealResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs,):
        client_name = row['customer']
        item_name = row['item']

        client, _ = Client.objects.get_or_create(username=client_name)
        item, _ = Item.objects.get_or_create(name=item_name)

        row['customer'] = client.pk
        row['item'] = item.pk

    def import_file(self, file, **kwargs):
        io_string = io.StringIO(file.read().decode())
        dataset = tablib.Dataset(
            headers=['customer', 'item', 'total', 'quantity', 'date']) \
            .load(io_string, format='csv')
        return self.import_data(dataset, **kwargs)

    class Meta:
        model = Deal
        skip_unchanged = True
        export_order = ('customer', 'item', 'total', 'quantity', 'date',)

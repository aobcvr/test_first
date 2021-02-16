from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .resources import DealResource
from .models import Deal


@admin.register(Deal)
class DealAdmin(ImportExportModelAdmin):
    list_display = ('id', 'customer', 'item', 'quantity', 'total', 'date',)
    resource_class = DealResource

    class Meta:
        model = Deal

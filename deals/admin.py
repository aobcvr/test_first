from django.contrib import admin
from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'item', 'quantity', 'total', 'date',)

    class Meta:
        model = Deal

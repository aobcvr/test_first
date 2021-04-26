import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField


class Deal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        "clients.Client",
        verbose_name=_("Клиент"),
        on_delete=models.CASCADE,
        related_name="deals",
    )
    item = models.ForeignKey(
        "items.Item",
        verbose_name=_("Наименование товара"),
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        _("Количество товара, шт"),
        default=1,
    )
    total = MoneyField(
        verbose_name=_("Сумма сделки"),
        max_digits=14,
        decimal_places=2,
        default_currency='USD'
    )
    date = models.DateTimeField(
        _("Дата и время регистрации сделки"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Сделка")
        verbose_name_plural = _("Сделки")

    def __str__(self):
        return "#{}".format(self.id)

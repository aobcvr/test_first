import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Deal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        'clients.Client', verbose_name=_('Клиент'), on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        'items.Item', verbose_name=_('Наименование товара'),
        on_delete=models.CASCADE,
    )
    total = models.PositiveIntegerField(
        _('Сумма сделки'),
    )
    date = models.DateTimeField(
        _("Дата и время регистрации сделки"), auto_now=True,
    )

    class Meta:
        verbose_name = _('Сделка')
        verbose_name_plural = _('Сделки')

    def __str__(self):
        return '#{}'.format(self.id)

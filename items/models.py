from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(_('Наименование товара'), max_length=256,)
    quantity = models.PositiveIntegerField(
        _('Количество товара, шт'),
    )
    price = models.PositiveIntegerField(
        _('Стоимость товара'),
    )

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return self.name

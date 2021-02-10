from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Client(AbstractUser):
    username = models.CharField(max_length=40, unique=True,)
    spent_money = models.PositiveIntegerField(
        _('Сумма потраченных денег за весь период'), default=0,
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def get_top_clients():
        return Client.objects.all().order_by('-spent_money')[:5]

    @property
    def get_gems(self):
        """Список общих купленных камней с хотя-бы одним покупателем.

        Desc:
            Список из названий камней, которые купили как минимум двое из
            списка 5 клиентов, потративших наибольшую сумму за весь период, и
            данный клиент является одним из этих покупателей.
        """
        instance_gems = set([deal.item.name for deal in self.deals.all()])

        top_clients = Client.get_top_clients()

        for client in top_clients:
            client_gems = set([deal.item.name for deal in self.deals.all()])

            common_stones = tuple(client_gems & instance_gems)

            if len(common_stones) > 0:
                return common_stones

        return None

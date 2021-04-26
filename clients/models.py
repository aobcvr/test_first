from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class Client(AbstractUser):
    username = models.CharField(
        max_length=40,
        unique=True,
    )
    spent_money = MoneyField(
        verbose_name=_("Сумма потраченных денег за весь период"),
        max_digits=14,
        decimal_places=2,
        default_currency='USD',
        default=Money(0, 'USD')
    )

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")

    @classmethod
    def get_leaderboard(cls, count=5):
        """
        Топ клиентов, потративших наибольшую сумму за весь период.
        """
        cache_key = 'client_get_leaderboard_{}'.format(count)

        if (cached_leaderboard := cache.get(cache_key)) is None:
            cached_leaderboard = Client.objects.filter(spent_money__gt=Money(0, 'USD')).order_by('-spent_money')[:count]
            cache.set(cache_key, cached_leaderboard, 60 * 5)
        return cached_leaderboard

    @property
    def bought_gems(self):
        """
        Камни, приобретенные хотя-бы раз данным клиентом.
        """
        bought_gems = [deal.item for deal in self.deals.select_related("item").distinct('item')]
        return bought_gems

    @property
    def get_gems(self):
        """
        Список из названий камней, которые купили как минимум двое из
        списка 5 клиентов, потративших наибольшую сумму за весь период, и
        данный клиент является одним из этих покупателей.
        """
        cache_key = 'client_get_gems_{}'.format(self.pk)
        leaderboard = Client.get_leaderboard().prefetch_related("deals")

        if self not in leaderboard:
            return []

        if (cached_get_gems := cache.get(cache_key)) is None:
            for leader in leaderboard:
                if leader.pk is self.pk:
                    continue

                if common_stones := set(leader.bought_gems) & set(self.bought_gems):
                    cached_get_gems = [item.name for item in common_stones]
                    cache.set(cache_key, cached_get_gems, 60 * 5)
        return cached_get_gems

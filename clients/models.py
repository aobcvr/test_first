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

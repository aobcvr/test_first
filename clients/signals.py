import logging

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from deals.models import Client

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Client)
def invalidate(instance, created, **kwargs):
    """Invalidate cache for get_gems and get_leaderboard"""
    pattern_list = (
        'client_get_gems_{}'.format(instance.pk),
        'client_get_leaderboard_*'.format(instance.pk),
    )

    for pattern in pattern_list:
        cache.delete(pattern)

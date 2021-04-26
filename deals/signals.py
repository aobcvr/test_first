import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from deals.models import Deal

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Deal)
def deal_update_spent_money(instance, created, **kwargs):
    """Update spent money for the buyer"""
    if created:
        try:
            customer = instance.customer
            customer.spent_money += instance.total
            customer.save(update_fields=('spent_money',))
        except:
            logger.exception('Unable to update spent money for buyer #{}'.format(instance.customer.pk))

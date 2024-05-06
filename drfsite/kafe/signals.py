from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Guests


@receiver(post_save, sender=Guests)
def update_guests_now(sender, instance, created, **kwargs):
    if instance.isPresent:
        table = instance.table
        table.guestsNow += 1
    else:
        table = instance.table
        if table.guestsNow > 0:
            table.guestsNow -= 1

    table.save()


@receiver(post_save, sender=Guests)
def increment_guests_def(sender, instance, created, **kwargs):
    if created:
        table = instance.table
        table.guestsDef += 1
        table.save()


@receiver(post_delete, sender=Guests)
def decrement_guests_def(sender, instance, **kwargs):
    table = instance.table
    table.guestsDef -= 1
    table.save()

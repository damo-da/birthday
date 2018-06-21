from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Person
from helpers.birthday_helper import get_random_superhero
from helpers.log import log


@receiver(pre_save, sender=Person)
def cb(sender, instance, *args, **kwargs):
    log('Saving {}'.format(str(instance)))

    if instance.hero is not None and instance.hero.gender is not instance.gender:
        log('Hero is of the wrong gender. Removing hero.')
        instance.hero = None

    if instance.hero is None:
        log('Assigning a random hero.')
        instance.hero = get_random_superhero(instance.gender)

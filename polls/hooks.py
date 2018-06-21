from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Person
from helpers.birthday_helper import get_random_superhero

@receiver(pre_save, sender=Person)
def cb(sender, instance, *args, **kwargs):

    if instance.hero is not None and instance.hero.gender is not instance.gender:
        instance.hero = None

    if instance.hero is None:
        instance.hero = get_random_superhero(instance.gender)

    print('pre saving')

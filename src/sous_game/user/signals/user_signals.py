from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import SousUser, Profile

@receiver(post_save, sender=SousUser)
def create_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        Profile.objects.create(user=instance)
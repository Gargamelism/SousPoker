from django.db import models

from sous_game.core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField("user.SousUser", on_delete=models.CASCADE, related_name="profile")

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    about = models.TextField(blank=True)
    avatar = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

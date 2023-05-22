from rest_framework import serializers

from sous_game.sous_auth.models import SousUser


class SousUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SousUser
        fields = ["url", "username", "email", "groups", "token"]

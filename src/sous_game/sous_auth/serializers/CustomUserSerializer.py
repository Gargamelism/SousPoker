from rest_framework import serializers

from sous_game.sous_auth.models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["url", "username", "email", "groups", "token"]

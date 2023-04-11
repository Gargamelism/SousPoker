from django.apps import apps as apps_conf
from rest_framework import serializers

from sous_game.sous_auth.models.CustomUser import CustomUser

auth_config = apps_conf.get_app_config("sous_auth")


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=auth_config.password_min_length,
        max_length=auth_config.password_max_length,
        write_only=True,
    )

    token = serializers.CharField(max_length=auth_config.jwt_token_max_length, read_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password", "token"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
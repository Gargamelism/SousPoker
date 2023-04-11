from django.apps import apps as apps_conf
from rest_framework import serializers

from sous_game.sous_auth.models.CustomUser import CustomUser

auth_config = apps_conf.get_app_config("sous_auth")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length = auth_config.password_min_length,
        max_length = auth_config.password_max_length,
        write_only = True,
        )

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password", "token",)
        read_only_fields = ("token",)

    def update(self, instance: CustomUser, validated_data: dict) -> CustomUser:
        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

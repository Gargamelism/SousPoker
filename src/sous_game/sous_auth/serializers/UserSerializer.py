from django.apps import apps as apps_conf
from rest_framework import serializers

from sous_game.sous_auth.models import SousUser
from sous_game.profiles.serializers import ProfileSerializer
from ..models import SousUser


auth_config = apps_conf.get_app_config("sous_auth")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=auth_config.password_min_length,
        max_length=auth_config.password_max_length,
        write_only=True,
    )

    profile = ProfileSerializer(write_only=True)
    about = serializers.CharField(source="profile.about", read_only=True)
    avatar = serializers.CharField(source="profile.avatar", read_only=True)

    class Meta:
        model = SousUser
        fields = (
            "email",
            "username",
            "password",
            "token",
            "profile",
            "about",
            "avatar",
        )
        read_only_fields = ("token",)

    def update(self, instance: SousUser, validated_data: dict) -> SousUser:
        password = validated_data.pop("password", None)

        profile_data = validated_data.pop("profile", {})

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)

        instance.profile.save()

        return instance

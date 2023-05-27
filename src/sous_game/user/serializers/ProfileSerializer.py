from rest_framework import serializers
from django.apps import apps as apps_conf

from ..models import Profile


profile_config = apps_conf.get_app_config("user")


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    about = serializers.CharField(allow_blank=True, required=False)
    avatar = serializers.URLField(allow_blank=True, required=False)

    class Meta:
        model = Profile
        fields = (
            "username",
            "about",
            "avatar",
        )
        read_only_fields = ("username",)

    def get_avatar(self, profile: Profile):
        avatar = profile.avatar
        if avatar:
            return avatar

        return profile_config.default_avatar

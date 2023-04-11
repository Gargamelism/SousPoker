from django.apps import apps as apps_conf
from django.contrib.auth import authenticate
from rest_framework import serializers

auth_config = apps_conf.get_app_config("sous_auth")


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length = 255, read_only = True)
    password = serializers.CharField(
        min_length = auth_config.password_min_length,
        max_length = auth_config.password_max_length,
        write_only = True,
        )
    token = serializers.CharField(max_length = 255, read_only = True)

    def validate(self, data: dict):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError(
                "An email address is required to log in."
            )

        if password is None:
            raise serializers.ValidationError(
                "A password is required to log in."
            )

        user = authenticate(username = email, password = password)
        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password was not found"
                )

        if not user.is_active:
            raise serializers.ValidationError(
                "This user has been deactivated."
                )

        return {
            "email": user.email,
            "username": user.username,
            "token": user.token
            }
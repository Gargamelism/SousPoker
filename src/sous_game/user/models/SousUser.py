import jwt
from django.apps import apps as apps_conf
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from datetime import datetime, timedelta


from sous_game.core.models import TimestampedModel
from sous_game.user.models import Profile


class SousUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if username is None:
            raise TypeError("Users must have a username")

        if email is None:
            raise TypeError("Users must have an email")

        if password is None:
            raise TypeError("Users must have a password")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class SousUser(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # USERNAME_FIELD describes the login field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = SousUserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        auth_config = apps_conf.get_app_config("user")

        jwt_expiration_days = auth_config.jwt_token_expiration
        expiration_date = datetime.now() + timedelta(days=jwt_expiration_days)

        jwt_encoding_algorithm = auth_config.jwt_encode_algorithm
        token = jwt.encode(
            {"id": self.pk, "exp": int(expiration_date.strftime("%s"))},
            settings.SECRET_KEY,
            algorithm=jwt_encoding_algorithm,
        )

        return token

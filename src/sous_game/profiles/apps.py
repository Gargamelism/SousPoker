from django.apps import AppConfig
import environ

# Initialise environment
env = environ.Env()
environ.Env.read_env()


class ProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sous_game.profiles"

    default_avatar = env("SOUS_PROFILE_DEFAULT_AVATAR")
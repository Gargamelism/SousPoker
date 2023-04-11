from django.apps import AppConfig
import environ

# Initialise environment
env = environ.Env()
environ.Env.read_env()


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sous_game.sous_auth"

    password_min_length = env.int("CUSTOM_USER_MIN_PW_LENGTH")
    password_max_length = env.int("CUSTOM_USER_MAX_PW_LENGTH")

    jwt_token_max_length = env.int("CUSTOM_USER_JWT_TOKEN_MAX_LENGTH")
    jwt_token_expiration = env.int("CUSTOM_USER_JWT_TOKEN_EXPIRATION_DAYS")
    jwt_encode_algorithm = env("CUSTOM_USER_JWT_TOKEN_ALGORITHM")

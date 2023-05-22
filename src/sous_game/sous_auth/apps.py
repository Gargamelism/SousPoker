from django.apps import AppConfig
import environ

# Initialise environment
env = environ.Env()
environ.Env.read_env()


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sous_game.sous_auth"
    label = "sous_auth"
    verbose_name = "Sous Auth"

    password_min_length = env.int("SOUS_USER_MIN_PW_LENGTH")
    password_max_length = env.int("SOUS_USER_MAX_PW_LENGTH")

    jwt_token_max_length = env.int("SOUS_USER_JWT_TOKEN_MAX_LENGTH")
    jwt_token_expiration = env.int("SOUS_USER_JWT_TOKEN_EXPIRATION_DAYS")
    jwt_encode_algorithm = env("SOUS_USER_JWT_TOKEN_ALGORITHM")

    def ready(self):
        import sous_game.sous_auth.signals.user_signals

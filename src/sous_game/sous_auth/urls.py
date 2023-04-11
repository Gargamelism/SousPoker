from django.urls import re_path

from sous_game.sous_auth.views import RegistrationApiView, LoginApiView, UserRetrieveUpdateApiView

app_name = "auth"

urlpatterns = [
    re_path(r"^user/?$", UserRetrieveUpdateApiView.as_view()),
    re_path(r"^users/?$", RegistrationApiView.as_view()),
    re_path(r"^users/login/?$", LoginApiView.as_view()),
]

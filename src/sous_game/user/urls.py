from django.urls import path, re_path

from .views import ProfileRetrieveApiView, UserRetrieveUpdateApiView, RegistrationApiView, LoginApiView

app_name = "user"
urlpatterns = [
    path("profiles/<str:username>/", ProfileRetrieveApiView.as_view(), name="retrieve"),
    re_path(r"^user/?$", UserRetrieveUpdateApiView.as_view()),
    re_path(r"^users/?$", RegistrationApiView.as_view()),
    re_path(r"^users/login/?$", LoginApiView.as_view()),
]
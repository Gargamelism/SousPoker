from django.urls import path

from .views import ProfileRetrieveApiView

app_name = "profiles"
urlpatterns = [
    path("profiles/<str:username>/", ProfileRetrieveApiView.as_view(), name="retrieve"),
]
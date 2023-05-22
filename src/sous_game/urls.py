from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from sous_game.sous_auth.views import GroupView, UserView


router = routers.DefaultRouter()
router.register(r"users", UserView.UserViewSet)
router.register(r"groups", GroupView.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include("sous_game.sous_auth.urls", namespace="auth")),
    path("api/", include("sous_game.profiles.urls", namespace="profiles")),
]

from rest_framework import viewsets, permissions

from sous_game.sous_auth.models import CustomUser
from sous_game.sous_auth.serializers.CustomUserSerializer import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-created_at")
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
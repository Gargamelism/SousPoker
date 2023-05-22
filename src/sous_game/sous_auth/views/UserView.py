from rest_framework import viewsets, permissions

from sous_game.sous_auth.models import SousUser
from sous_game.sous_auth.serializers import SousUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = SousUser.objects.all().order_by("-created_at")
    serializer_class = SousUserSerializer
    permission_classes = [permissions.IsAuthenticated]
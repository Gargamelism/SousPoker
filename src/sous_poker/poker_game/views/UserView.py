from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from sous_poker.poker_game.serializers.UserSerializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
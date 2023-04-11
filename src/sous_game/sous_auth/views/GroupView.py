from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from sous_game.sous_auth.serializers.GroupSerializer import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
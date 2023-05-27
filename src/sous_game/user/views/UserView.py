from rest_framework import viewsets, permissions

from ..models import SousUser
from ..serializers import SousUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = SousUser.objects.all().order_by("-created_at")
    serializer_class = SousUserSerializer
    permission_classes = [permissions.IsAuthenticated]
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any

from sous_game.sous_auth.renderers import UserJSONRenderer
from sous_game.sous_auth.serializers import UserSerializer


class UserRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer_data = request.data.get("user", {})
        serializer = self.serializer_class(request.user, data = serializer_data, partial = True)

        serializer.is_valid(raise_exception = True)

        serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)

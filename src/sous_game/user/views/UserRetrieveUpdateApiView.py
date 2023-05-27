from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any

from ..renderers import UserJsonRenderer
from ..serializers import UserSerializer


class UserRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJsonRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user_data = request.data.get("user", {})

        serializer_data = {
            "username": user_data.get("username", request.user.username),
            "email": user_data.get("email", request.user.email),

            "profile": {
                "about": user_data.get("about", request.user.profile.about),
                "avatar": user_data.get("avatar", request.user.profile.avatar),
            }
        }

        serializer = self.serializer_class(request.user, data = serializer_data, partial = True)

        serializer.is_valid(raise_exception = True)

        serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)

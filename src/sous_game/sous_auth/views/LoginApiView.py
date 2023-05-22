from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request

from sous_game.sous_auth.renderers import UserJsonRenderer
from sous_game.sous_auth.serializers.LoginSerializer import LoginSerializer


class LoginApiView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJsonRenderer,)
    serializer_class = LoginSerializer

    def post(self, request: Request):
        user = request.data.get("user", {})
        
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
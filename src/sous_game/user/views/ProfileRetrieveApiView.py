from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from ..models import Profile
from ..renderers import ProfileJsonRenderer
from ..serializers import ProfileSerializer
from ..exceptions import ProfileDoesNotExist


class ProfileRetrieveApiView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (ProfileJsonRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request: Request, username: str, *args, **kwargs) -> Response:
        try:
            profile = Profile.objects.select_related("user").get(
                user__username=username
            )
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

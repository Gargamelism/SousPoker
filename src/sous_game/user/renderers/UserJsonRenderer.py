import json
from typing import Dict

from sous_game.core.renderers import BaseJsonRenderer


class UserJsonRenderer(BaseJsonRenderer):
    object_label = "user"
    pagination_object_label = "users"
    pagination_count_label = "users-count"

    def render(self, data: dict, media_type: str = None, renderer_context: Dict = None):
        token = data.get("token", None)

        if token is not None and isinstance(token, bytes):
            data["token"] = token.decode("utf-8")

        return super(UserJsonRenderer, self).render(data)

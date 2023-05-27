from sous_game.core.renderers import BaseJsonRenderer


class ProfileJsonRenderer(BaseJsonRenderer):
    object_label = "profile"
    pagination_object_label = "profiles"
    pagination_count_label = "profiles-count"

    def render(self, data, media_type=None, renderer_context=None):
        return super(ProfileJsonRenderer, self).render(data)
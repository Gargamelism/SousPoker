import json

from rest_framework.renderers import JSONRenderer


class BaseJsonRenderer(JSONRenderer):
    charset = "utf-8"
    object_label = "BASE_JSON_RENDERER"

    def render(self, data: dict, media_type=None, renderer_context=None):
        if not isinstance(data, dict):
            data = {
                "errors": [
                    "Incorrect type. Expected a dictionary, but got a {0}.".format(
                        type(data).__name__
                    )
                ]
            }

        errors = data.get("errors", None)

        if errors is not None:
            return super(BaseJsonRenderer, self).render(data)

        return json.dumps(
            {
                self.object_label: data,
            }
        )

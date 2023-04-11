from rest_framework.views import exception_handler
from rest_framework.response import Response
from typing import Optional


def core_exception_handler(exception: Exception, context: dict) -> Optional[Response]:
    response = exception_handler(exception, context)

    handlers = {
        "ValidationError": _handle_generic_error,
        "NotFound": _handle_generic_error,
        "PermissionDenied": _handle_generic_error,
        "AuthenticationFailed": _handle_generic_error,
        "NotAuthenticated": _handle_generic_error,
        "MethodNotAllowed": _handle_generic_error,
        }

    exception_class = exception.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exception, context, response)

    return response


def _handle_generic_error(exception: Exception, context: dict, response: Response) -> Response:
    return Response(
        {
            "errors": response.data
            }, status = response.status_code
        )

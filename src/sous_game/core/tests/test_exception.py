import unittest
from rest_framework.exceptions import ValidationError, ErrorDetail

from ..exceptions import core_exception_handler


class ExceptionTest(unittest.TestCase):
    def test_core_exception_handler_handles_generic_error_with_detail(self):
        # Arrange
        exception = ValidationError("Test Error")
        context = {}

        # Act
        result = core_exception_handler(exception, context)

        # Assert
        assert result.status_code == 400
        assert result.status_text == "Bad Request"
        assert result.data == {"errors": ["Test Error"]}

    def test_core_exception_handler_handles_generic_error_with_detail_and_code(self):
        # Arrange
        exception = ValidationError({"test": "Test Error"}, code="test_code")
        context = {}

        # Act
        result = core_exception_handler(exception, context)

        # Assert
        assert result.status_code == 400
        assert result.status_text == "Bad Request"
        assert result.data == {"errors": {"test": "Test Error"}}
        assert result.data["errors"]["test"].code == "test_code"

    def test_core_exception_handler_handles_unknown_error(self):
        # Arrange
        exception = Exception("Test Error")
        context = {}

        # Act
        result = core_exception_handler(exception, context)

        # Assert
        assert result.status_code == 500
        assert result.status_text == "Internal Server Error"
        assert result.data == {"errors": ["A server error occurred"]}

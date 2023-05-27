import unittest
import json

from ..renderers import BaseJsonRenderer


class BaseJsonRendererTests(unittest.TestCase):
    def test_render_simple_dict(self):
        data = {"key": "value"}
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = json.dumps({renderer.object_label: {"key": "value"}})
        self.assertEqual(result, expected)

    def test_render_list(self):
        data = ["item1", "item2", "item3"]
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = (
            b'{"errors":["Incorrect type. Expected a dictionary, but got a list."]}'
        )
        self.assertEqual(result, expected)

    def test_render_nested_dict(self):
        data = {"key1": {"nested_key": "nested_value"}, "key2": "value2"}
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = json.dumps(
            {
                renderer.object_label: {
                    "key1": {"nested_key": "nested_value"},
                    "key2": "value2",
                }
            }
        )
        self.assertEqual(result, expected)

    def test_render_special_characters(self):
        data = {"key": 'value with "quotes"'}
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = json.dumps({renderer.object_label: {"key": 'value with "quotes"'}})
        self.assertEqual(result, expected)

    def test_render_numbers(self):
        data = {"integer": 123, "float": 3.14}
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = json.dumps({renderer.object_label: {"integer": 123, "float": 3.14}})
        self.assertEqual(result, expected)

    def test_render_booleans(self):
        data = {"true_value": True, "false_value": False}
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = json.dumps(
            {renderer.object_label: {"true_value": True, "false_value": False}}
        )
        self.assertEqual(result, expected)

    def test_render_with_errors(self):
        data = {"errors": ["Error 1", "Error 2"]}
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = b'{"errors":["Error 1","Error 2"]}'
        self.assertEqual(result, expected)

    def test_render_with_errors_and_data(self):
        data = {"errors": ["Error 1", "Error 2"], "key": "value"}
        renderer = BaseJsonRenderer()
        result = renderer.render(data)
        expected = b'{"errors":["Error 1","Error 2"],"key":"value"}'
        self.assertEqual(result, expected)

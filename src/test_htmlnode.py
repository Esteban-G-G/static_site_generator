import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_no_props(self):
        """Test props_to_html() when there are no properties."""
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        """Test props_to_html() with a single attribute."""
        node = HTMLNode("a", "Click me", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple_props(self):
        """Test props_to_html() with multiple attributes."""
        node = HTMLNode("a", "Click me", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()

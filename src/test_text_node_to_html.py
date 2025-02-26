import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class test_text_node_to_html_node_text(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        """Test conversion of a plain text node."""
        text_node = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Hello")

    def test_text_node_to_html_node_bold(self):
        """Test conversion of a bold text node."""
        text_node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold Text</b>")

    def test_text_node_to_html_node_italic(self):
        """Test conversion of an italic text node."""
        text_node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic Text</i>")

    def test_text_node_to_html_node_code(self):
        """Test conversion of a code text node."""
        text_node = TextNode("print('Hello')", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>print('Hello')</code>")

    def test_text_node_to_html_node_link(self):
        """Test conversion of a link text node."""
        text_node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">Boot.dev</a>')

    def test_text_node_to_html_node_image(self):
        """Test conversion of an image text node."""
        text_node = TextNode("An image", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.png" alt="An image"></img>')

    def test_text_node_to_html_node_invalid_type(self):
        """Test that an unsupported TextType raises an error."""
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Invalid", None))

    def test_text_node_to_html_node_link_missing_url(self):
        """Test that a LINK text node without a URL raises an error."""
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("No URL", TextType.LINK))

    def test_text_node_to_html_node_image_missing_url(self):
        """Test that an IMAGE text node without a URL raises an error."""
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("No URL", TextType.IMAGE))

if __name__ == "__main__":
    unittest.main()
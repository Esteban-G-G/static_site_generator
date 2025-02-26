import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_requires_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leafnode_renders_raw_text(self):
        node=LeafNode(None, "Test text")
        self.assertEqual(node.to_html(), "Test text")

    def test_leafnode_renders_html(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_leafnode_renders_with_attributes(self):
        node = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main( )
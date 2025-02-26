import unittest
from textnode import TextNode, TextType, split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter_bold(self):
        """Test splitting a text node containing bold markdown."""
        node = TextNode("This is **bold text** in a sentence", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in a sentence", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_italic(self):
        """Test splitting a text node containing italic markdown."""
        node = TextNode("This is _italic text_ in a sentence", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in a sentence", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_code(self):
        """Test splitting a text node containing inline code markdown."""
        node = TextNode("This is `code` in a sentence", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in a sentence", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_no_delimiters(self):
        """Test a text node with no delimiters remains unchanged."""
        node = TextNode("This has no formatting.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [node])

    def test_split_nodes_delimiter_unmatched_delimiter(self):
        """Test that an error is raised if a delimiter is unmatched."""
        node = TextNode("This is **bold without closure", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_split_nodes_delimiter_multiple_splits(self):
        """Test that multiple inline elements in a single string work correctly."""
        node = TextNode("This is **bold** and this is _italic_", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ])

    def test_split_nodes_delimiter_leaves_non_text_nodes(self):
        """Test that non-text nodes remain unchanged."""
        text_node = TextNode("Text **bold** more text", TextType.TEXT)
        bold_node = TextNode("Already bold", TextType.BOLD)

        new_nodes = split_nodes_delimiter([text_node, bold_node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("Text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" more text", TextType.TEXT),
            bold_node,  # Should remain unchanged
        ])

if __name__ == "__main__":
    unittest.main()

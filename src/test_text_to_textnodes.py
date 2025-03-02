import unittest
from textnode import TextNode, TextType, text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes_basic(self):
        """Test converting markdown text with bold, italic, code, images, and links."""
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(nodes, expected)

    def test_text_to_textnodes_no_markdown(self):
        """Test text with no markdown remains unchanged."""
        text = "This is plain text with no formatting."
        nodes = text_to_textnodes(text)

        self.assertListEqual(nodes, [TextNode(text, TextType.TEXT)])

    def test_text_to_textnodes_only_bold(self):
        """Test text with only bold formatting."""
        text = "**bold**"
        nodes = text_to_textnodes(text)

        self.assertListEqual(nodes, [TextNode("bold", TextType.BOLD)])

    def test_text_to_textnodes_only_italic(self):
        """Test text with only italic formatting."""
        text = "_italic_"
        nodes = text_to_textnodes(text)

        self.assertListEqual(nodes, [TextNode("italic", TextType.ITALIC)])

    def test_text_to_textnodes_only_code(self):
        """Test text with only inline code."""
        text = "`code`"
        nodes = text_to_textnodes(text)

        self.assertListEqual(nodes, [TextNode("code", TextType.CODE)])

    def test_text_to_textnodes_only_image(self):
        """Test text with only an image."""
        text = "![alt text](https://example.com/image.jpg)"
        nodes = text_to_textnodes(text)

        self.assertListEqual(nodes, [TextNode("alt text", TextType.IMAGE, "https://example.com/image.jpg")])

    def test_text_to_textnodes_only_link(self):
        """Test text with only a link."""
        text = "[link text](https://example.com)"
        nodes = text_to_textnodes(text)

        self.assertListEqual(nodes, [TextNode("link text", TextType.LINK, "https://example.com")])

if __name__ == "__main__":
    unittest.main()

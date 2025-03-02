import unittest
from textnode import split_nodes_image, split_nodes_link, TextType, TextNode

class TestSplitNodes(unittest.TestCase):

    def test_split_images_single(self):
        """Test splitting a single image."""
        node = TextNode("Check this out ![image](https://example.com/image.jpg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])

        self.assertListEqual(new_nodes, [
            TextNode("Check this out ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.jpg")
        ])

    def test_split_images_multiple(self):
        """Test splitting multiple images."""
        node = TextNode(
            "Here is ![dog](https://example.com/dog.jpg) and ![cat](https://example.com/cat.jpg)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(new_nodes, [
            TextNode("Here is ", TextType.TEXT),
            TextNode("dog", TextType.IMAGE, "https://example.com/dog.jpg"),
            TextNode(" and ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "https://example.com/cat.jpg")
        ])

    def test_split_images_no_images(self):
        """Test no images return the same node."""
        node = TextNode("No images here.", TextType.TEXT)
        new_nodes = split_nodes_image([node])

        self.assertListEqual(new_nodes, [node])

    def test_split_links_single(self):
        """Test splitting a single link."""
        node = TextNode("Visit [Google](https://google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertListEqual(new_nodes, [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com")
        ])

    def test_split_links_multiple(self):
        """Test splitting multiple links."""
        node = TextNode(
            "Go to [GitHub](https://github.com) and [Twitter](https://twitter.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(new_nodes, [
            TextNode("Go to ", TextType.TEXT),
            TextNode("GitHub", TextType.LINK, "https://github.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Twitter", TextType.LINK, "https://twitter.com")
        ])

    def test_split_links_no_links(self):
        """Test no links return the same node."""
        node = TextNode("No links here.", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertListEqual(new_nodes, [node])

if __name__ == "__main__":
    unittest.main()

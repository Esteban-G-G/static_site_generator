import unittest
from textnode import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
            """Test extracting multiple markdown images."""
            text = "Look at this ![dog](https://example.com/dog.jpg) and this ![cat](https://example.com/cat.jpg)."
            matches = extract_markdown_images(text)
            self.assertListEqual([
                ("dog", "https://example.com/dog.jpg"),
                ("cat", "https://example.com/cat.jpg")
            ], matches)

    def test_extract_markdown_images_no_images(self):
        """Test that no images return an empty list."""
        text = "This has no images, just text."
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        """Test extracting a single markdown link."""
        matches = extract_markdown_links("This is a [link](https://www.example.com)")
        self.assertListEqual([("link", "https://www.example.com")], matches)

    def test_extract_markdown_links_multiple(self):
        """Test extracting multiple markdown links."""
        text = "Here are links: [Google](https://google.com) and [GitHub](https://github.com)."
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("Google", "https://google.com"),
            ("GitHub", "https://github.com")
        ], matches)

    def test_extract_markdown_links_no_links(self):
        """Test that no links return an empty list."""
        text = "No links here!"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links_ignores_images(self):
        """Ensure that image markdown does not get picked up as a link."""
        text = "Here is an image ![alt text](https://example.com/image.jpg) and a link [Example](https://example.com)."
        matches = extract_markdown_links(text)
        self.assertListEqual([("Example", "https://example.com")], matches)

if __name__ == "__main__":
    unittest.main()
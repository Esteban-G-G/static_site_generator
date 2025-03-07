import unittest
from textnode import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extract_valid_title(self):
        self.assertEqual(extract_title("# My Title"), "My Title")

    def test_extract_title_with_spaces(self):
        self.assertEqual(extract_title("#    Spaced Title   "), "Spaced Title")

    def test_extract_title_multiline(self):
        md = """# First Title
        ## Second Title
        """
        self.assertEqual(extract_title(md), "First Title")

    def test_no_title_raises_exception(self):
        with self.assertRaises(ValueError):
            extract_title("This has no title.")

if __name__ == "__main__":
    unittest.main()

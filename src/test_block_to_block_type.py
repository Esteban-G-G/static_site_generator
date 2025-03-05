import unittest
from textnode import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_block_type_heading(self):
        """Test heading detection."""
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Small heading"), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        """Test code block detection."""
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        """Test quote block detection."""
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        """Test unordered list detection."""
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2\n- Item 3"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        """Test ordered list detection."""
        self.assertEqual(block_to_block_type("1. First item\n2. Second item\n3. Third item"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        """Test that unrecognized blocks default to paragraph."""
        self.assertEqual(block_to_block_type("This is a normal paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("No special markdown formatting here."), BlockType.PARAGRAPH)

    def test_block_to_block_type_malformed_list(self):
        """Test lists that are malformed should be paragraphs."""
        self.assertEqual(block_to_block_type("1. First item\n3. Skipped number"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("- Item 1\n* Mixed bullets"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()

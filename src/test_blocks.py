import unittest

from blocks import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_base_case(self):
        markdown = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block\n* This is a list item\n* This is another list item
        """

        expected_result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        result = markdown_to_blocks(markdown)

        self.assertListEqual(expected_result, result)

class TestBlockToBlockType(unittest.TestCase):
    def normal_paragraph(self):
        input = "This is a start of a paragraph.\nIt continues here."
        expected_result = "paragraph"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)

    def test_heading(self):
        input = "# This is a heading"
        expected_result = "heading"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)
    
    def test_multiple_headings(self):
        input = "#### This is a different heading"
        expected_result = "heading"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)
    
    def test_code(self):
        input = "```\nThis is a code block\n```"
        expected_result = "code"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)

    def test_quote(self):
        input = "> This is a quote block\n>It continues to the next line here."
        expected_result = "quote"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)
    
    def test_unordered_list_asterisk(self):
        input = "* This is a start of an unordered list\n* It continues to the next line."
        expected_result = "unordered_list"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)
    
    def test_unordered_list_dash(self):
        input = "- This is a start of an unordered list\n- It continues to the next line."
        expected_result = "unordered_list"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)

    def test_ordered_list(self):
        input = "1. This is a start of an ordered list\n2. It continues to the next line."
        expected_result = "ordered_list"
        result = block_to_block_type(input)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()
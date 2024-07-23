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

if __name__ == "__main__":
    unittest.main()
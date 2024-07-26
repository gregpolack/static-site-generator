import unittest

from blocks import *

class TestExtractTitle(unittest.TestCase):
    def test_base_case(self):
        md = "# Hello"

        expected_result = "Hello"
        result = extract_title(md)

        self.assertEqual(expected_result, result)

    def test_longer_md(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

"""

        expected_result = "This is a heading"
        result = extract_title(md)

        self.assertEqual(expected_result, result)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_base_case(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        expected_result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        result = markdown_to_blocks(md)

        self.assertListEqual(expected_result, result)

    def test_quotes(self):
        md = """
# This is a heading

>This is a line from a quote
>This is another one
"""

        expected_result = [
            "# This is a heading",
            ">This is a line from a quote\n>This is another one"
        ]
        result = markdown_to_blocks(md)

        self.assertListEqual(expected_result, result)

    def test_ordered_list(self):
        md = """
# This is a heading

1. This is the first list item
2. This is the second one
"""

        expected_result = [
            "# This is a heading",
            "1. This is the first list item\n2. This is the second one"
        ]
        result = markdown_to_blocks(md)

        self.assertListEqual(expected_result, result)
    
    def test_unordered_list(self):
        md = """
# This is a heading

- This is the first list item
- This is the second one
"""

        expected_result = [
            "# This is a heading", 
            "- This is the first list item\n- This is the second one"
        ]
        result = markdown_to_blocks(md)

        self.assertListEqual(expected_result, result)
    
    def test_code(self):
        md = """
# This is a heading

```
This is a code block
```
"""
        expected_result = [
            "# This is a heading",
            "```\nThis is a code block\n```"
        ]
        result = markdown_to_blocks(md)

        self.assertListEqual(expected_result, result)

class TestMarkdownToHTMLNode(unittest.TestCase):
    def base_case(self):
        md = """
This is a regular paragraph
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected_result = "<div><p>This is a regular paragraph</p></div>"

        self.assertEqual(expected_result, result)
    
    def test_heading(self):
        md = """
# This is a heading

This is a regular paragraph
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected_result = "<div><h1>This is a heading</h1><p>This is a regular paragraph</p></div>"

        self.assertEqual(expected_result, result)

    def test_smaller_heading(self):
        md = """
# This is a big heading

This is a regular paragraph

###### This is a smaller heading
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected_result = "<div><h1>This is a big heading</h1><p>This is a regular paragraph</p><h6>This is a smaller heading</h6></div>"

        self.assertEqual(expected_result, result)
    
    def test_quoteblock(self):
        md = """
# This is a heading

>This is a line of a quote
>This is the next line of it
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected_result = "<div><h1>This is a heading</h1><blockquote>This is a line of a quote This is the next line of it</blockquote></div>"

        self.assertEqual(expected_result, result)
    
    def test_codeblock(self):
        md = """
# This is a heading

```
This is a code block
This is its second line
```
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected_result = "<div><h1>This is a heading</h1><code><pre>This is a code block This is its second line</pre></code></div>"

        self.assertEqual(expected_result, result)
    
    def test_ordered_list(self):
        md = """
# This is a heading

1. First item
2. Second item
3. Third item
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected_result = "<div><h1>This is a heading</h1><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"

        self.assertEqual(expected_result, result)
    
    def test_unordered_list(self):
        md = """
# This is a heading

* First item
* Second item

- Different list first item
- Different list second item
"""
        node = markdown_to_html_node(md)
        result = node.to_html()
        expected_result = "<div><h1>This is a heading</h1><ul><li>First item</li><li>Second item</li></ul><ul><li>Different list first item</li><li>Different list second item</li></ul></div>"

        self.assertEqual(expected_result, result)

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
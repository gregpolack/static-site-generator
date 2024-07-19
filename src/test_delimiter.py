import unittest
from textnode import TextNode

from delimiter import split_nodes_delimiter

class TestDelimiter(unittest.TestCase):
    def test_base_case(self):
        node = [TextNode("This is text with a `code block` word", "text")]
        expected_result = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
        ]
        result = split_nodes_delimiter(node, "`", "code")
        
        self.assertListEqual(expected_result, result)
    
    def test_bold(self):
        node = [TextNode("This is text with a **bold** word", "text")]
        expected_result = [
            TextNode("This is text with a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" word", "text")
        ]
        result = split_nodes_delimiter(node, "**", "bold")
        
        self.assertListEqual(expected_result, result)
    
    def test_double_bold(self):
        node = [TextNode("This is text with a **bold** word and **another one**", "text")]
        expected_result = [
            TextNode("This is text with a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" word and ", "text"),
            TextNode("another one", "bold")
        ]
        result = split_nodes_delimiter(node, "**", "bold")
        
        self.assertListEqual(expected_result, result)
    
    def test_italic(self):
        node = [TextNode("This is text with an *italic* word", "text")]
        expected_result = [
            TextNode("This is text with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word", "text")
        ]
        result = split_nodes_delimiter(node, "*", "italic")
        
        self.assertListEqual(expected_result, result)
    
    def test_non_text_types(self):
        nodes = [
            TextNode("This whole sentence is in italic", "italic"),
            TextNode("This one is bold", "bold"),
            TextNode("This one has some `code` in it", "text")
        ]
        expected_result = [ 
            TextNode("This whole sentence is in italic", "italic"),
            TextNode("This one is bold", "bold"),
            TextNode("This one has some ", "text"),
            TextNode("code", "code"),
            TextNode(" in it", "text")
        ]
        result = split_nodes_delimiter(nodes, "`", "code")

        self.assertListEqual(expected_result, result)

    def test_missing_delimiter(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a **bold block of text", "text")
            split_nodes_delimiter([node], "**", "bold")
    
    def test_mismatching_delimiters(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a **bold block` of text", "text")
            split_nodes_delimiter([node], "**", "bold")
    
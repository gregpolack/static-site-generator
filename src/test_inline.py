import unittest
from textnode import TextNode

from inline import *

class TestSplitNodesDelimiter(unittest.TestCase):
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

class TestExtractMarkdownImages(unittest.TestCase):
    def test_base_case(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(text)

        self.assertListEqual(expected_result, result)
    
    def test_image_at_start(self):
        text = "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(text)

        self.assertListEqual(expected_result, result)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_base_case(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        result = extract_markdown_links(text)

        self.assertListEqual(expected_result, result)
    
    def test_link_at_start(self):
        text = "[website](https://www.rickroll.com)"
        expected_result = [("website", "https://www.rickroll.com")]
        result = extract_markdown_links(text)

        self.assertListEqual(expected_result, result)

class TestSplitNodesImage(unittest.TestCase):
    def test_base_case(self):
        node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        "text"
    )
        expected_result = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        result = split_nodes_image([node])

        self.assertListEqual(expected_result, result)

    def test_multiple_nodes(self):
        node1 = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "text"
        )
        node2 = TextNode(
            "This is another text with an image of ![Michael Scott](https://i.imgur.com/aBw08gY.gif) and ![Dwight](https://i.imgur.com/ScH7$hT.gif)",
            "text"
        )
        expected_result = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("This is another text with an image of ", "text"),
            TextNode("Michael Scott", "image", "https://i.imgur.com/aBw08gY.gif"),
            TextNode(" and ", "text"),
            TextNode("Dwight", "image", "https://i.imgur.com/ScH7$hT.gif")
        ]
        result = split_nodes_image([node1, node2])

        self.assertListEqual(expected_result, result)
    
    def test_only_images(self):
        node1 = TextNode(
            "![rick roll](https://i.imgur.com/aKaOqIh.gif)![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "text"
        )
        node2 = TextNode(
            "![Michael Scott](https://i.imgur.com/aBw08gY.gif)![Dwight](https://i.imgur.com/ScH7$hT.gif)",
            "text"
        )
        expected_result = [
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("Michael Scott", "image", "https://i.imgur.com/aBw08gY.gif"),
            TextNode("Dwight", "image", "https://i.imgur.com/ScH7$hT.gif")
        ]
        result = split_nodes_image([node1, node2])

        self.assertListEqual(expected_result, result)
    
    def test_only_text(self):
        node1 = TextNode("This is some text", "text")
        node2 = TextNode("This is another piece of text", "text")

        expected_result = [node1, node2]
        result = split_nodes_image([node1, node2])

        self.assertEqual(expected_result, result) 

class TestSplitNodesLink(unittest.TestCase):
    def test_base_case(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text"
        )
        expected_result = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        ]
        result = split_nodes_link([node])

        self.assertListEqual(expected_result, result)
    
    def test_multiple_nodes(self):
        node1 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text"
        )
        node2 = TextNode(
            "This is another text with a link [to facebook](https://www.facebook.com) and [to twitter](https://www.twitter.com)",
            "text"
        )
        expected_result = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
            TextNode("This is another text with a link ", "text"),
            TextNode("to facebook", "link", "https://www.facebook.com"),
            TextNode(" and ", "text"),
            TextNode("to twitter", "link", "https://www.twitter.com"),
        ]
        result = split_nodes_link([node1, node2])

        self.assertListEqual(expected_result, result)
    
    def test_only_links(self):
        node1 = TextNode(
            "[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",
            "text"
        )
        node2 = TextNode(
            "[to facebook](https://www.facebook.com)[to twitter](https://www.twitter.com)",
            "text"
        )
        expected_result = [
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
            TextNode("to facebook", "link", "https://www.facebook.com"),
            TextNode("to twitter", "link", "https://www.twitter.com")
        ]
        result = split_nodes_link([node1, node2])

        self.assertListEqual(expected_result, result)
    
    def test_only_text(self):
        node1 = TextNode("This is some text", "text")
        node2 = TextNode("This is another piece of text", "text")

        expected_result = [node1, node2]
        result = split_nodes_link([node1, node2])

        self.assertEqual(expected_result, result)
import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node, which is cooler", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)
        
    def test_not_eq_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_number(self):
        node = TextNode("This is a text node", 6, "https://boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://boot.dev")
        self.assertNotEqual(node, node2)
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", "text", "https://boot.dev")
        expected_result = LeafNode(None, node.text)
        result = text_node_to_html_node(node)
        
        self.assertEqual(result, expected_result)
    
    def test_bold(self):
        node = TextNode("This is a text node", "b", "https://boot.dev")
        expected_result = LeafNode("b", node.text)
        result = text_node_to_html_node(node)
        
        self.assertEqual(result, expected_result)
    
    def test_italic(self):
        node = TextNode("This is a text node", "i", "https://boot.dev")
        expected_result = LeafNode("i", node.text)
        result = text_node_to_html_node(node)
        
        self.assertEqual(result, expected_result)
    
    def test_code(self):
        node = TextNode("This is a text node", "code", "https://boot.dev")
        expected_result = LeafNode("code", node.text)
    
        self.assertEqual(text_node_to_html_node(node), expected_result)

    def test_link(self):
        node = TextNode("This is a link", "a", "https://boot.dev")
        expected_result = LeafNode("a", node.text, {"href": {node.url}})
    
        self.assertEqual(text_node_to_html_node(node), expected_result)
    
    def test_img(self):
        node = TextNode("This is an image", "img", "https://boot.dev")
        expected_result = LeafNode("img", "", {"src": {node.url}, "alt": {node.text}})
    
        self.assertEqual(text_node_to_html_node(node), expected_result)

if __name__ == "__main__":
    unittest.main()
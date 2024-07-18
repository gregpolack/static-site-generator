import unittest

from textnode import TextNode
from main import text_node_to_html_node
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
        result = LeafNode("b", node.text)
        self.assertEqual(text_node_to_html_node(node), result)

if __name__ == "__main__":
    unittest.main()
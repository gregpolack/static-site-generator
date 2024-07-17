import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "This is some text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"' )

    def test_props_space(self):
        node = HTMLNode("p", "This is some text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"' )

    def test_props_int(self):
        node = HTMLNode("p", "This is some text", None, {"href": "https://www.google.com", "target": 6})
        self.assertNotEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"' )

if __name__ == "__main__":
    unittest.main()

class TestLeafNode(unittest.TestCase):
    def test_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), result)
   
    def test_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        result = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), result)
        
if __name__ == "__main__":
    unittest.main()
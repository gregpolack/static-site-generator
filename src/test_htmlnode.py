import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_html(self):
        node = HTMLNode("p", "This is some text", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)

    def test_html_space(self):
        node = HTMLNode("p", "This is some text", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_result = 'href="https://www.google.com" target="_blank"'
        self.assertNotEqual(node.props_to_html(), expected_result )

    def test_html_int(self):
        node = HTMLNode("p", "This is some text", None, {"href": "https://www.google.com", "target": 6})
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertNotEqual(node.props_to_html(), expected_result )
    
    def test_repr(self):
        node = HTMLNode('p', 'This is some text', None, {'href': 'https://www.google.com', 'target': '_blank'})
        expected_result = "HTMLNode(p, This is some text, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual (repr(node), expected_result)

class TestLeafNode(unittest.TestCase):
    def test_base(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_result = '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), expected_result)
   
    def test_anchor(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        expected_result = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected_result)

    def test_no_value(self):
        node = LeafNode("a", None, {"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_no_tag(self):
        node = LeafNode(None, "Normal text")
        result = "Normal text"
        self.assertEqual(node.to_html(), result)

    def test_repr(self):
        node = LeafNode('a', 'Click me!', {'href': 'https://www.google.com', 'target': '_blank'})
        expected_result = "LeafNode(a, Click me!, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected_result)
    

class TestParentNode(unittest.TestCase):
    def test_base(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_nested(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text")
                    ]
                )
            ]
        )
        expected_result = "<p><b>Bold text</b><p>Normal text<i>italic text</i></p></p>"
        self.assertEqual(node.to_html(), expected_result)
    
    def test_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode("p")
        with self.assertRaises(ValueError):
            node.to_html()

    
    def test_repr(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text")
            ]
        )
        expected_result = "ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None)], None)"
        self.assertEqual(repr(node), expected_result)

        
if __name__ == "__main__":
    unittest.main()
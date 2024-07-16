import unittest

from htmlnode import HTMLNode

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
import unittest

from leafnode import LeafNode

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
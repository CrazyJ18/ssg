import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        target = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), target)
    
    def test_props_to_html2(self):
        node = HTMLNode("h1", "Title")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html3(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "here"})
        target = ' href="https://www.boot.dev" target="here"'
        self.assertEqual(node.props_to_html(), target)
    
    def test_to_html(self):
        node = HTMLNode("h1", "Title")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
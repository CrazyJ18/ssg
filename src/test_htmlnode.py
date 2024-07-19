import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_to_html2(self):
        node = LeafNode("p", "This is a paragraph of text.")
        target = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), target)

    def test_to_html3(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        target = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), target)

    def test_to_html4(self):
        node = LeafNode(value="This is a raw paragraph of text.")
        target = "This is a raw paragraph of text."
        self.assertEqual(node.to_html(), target)

    def test_to_html5(self):
        node = LeafNode("img", props={"src":"url/of/image.jpg", "alt":"Description of image"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html6(self):
        node = LeafNode("li", "Item 1")
        target = "<li>Item 1</li>"
        self.assertEqual(node.to_html(), target)


if __name__ == "__main__":
    unittest.main()
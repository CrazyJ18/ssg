import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node = LeafNode(
            "img", 
            props={"src":"url/of/image.jpg", "alt":"Description of image"}
            )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html5_1(self):
        node = LeafNode(
            "img", 
            "",
            props={"src":"url/of/image.jpg", "alt":"Description of image"}
            )
        target = '<img src="url/of/image.jpg" alt="Description of image">'
        self.assertEqual(node.to_html(), target)

    def test_to_html6(self):
        node = LeafNode("li", "Item 1")
        target = "<li>Item 1</li>"
        self.assertEqual(node.to_html(), target)
    
    def test_to_html7(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        target = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), target)
    
    def test_to_html8(self):
        node = ParentNode(
            "p",
            [
                LeafNode("h1", "List"),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "apples"),
                        LeafNode("li", "bananas"),
                    ]
                )
            ]
        )
        target = "<p><h1>List</h1><ul><li>apples</li><li>bananas</li></ul></p>"
        self.assertEqual(node.to_html(), target)

    def test_to_html9(self):
        node = ParentNode("p")
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
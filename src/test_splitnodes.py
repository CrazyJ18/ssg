import unittest

from splitnodes import *

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        target = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text)
            ]
        self.assertEqual(new_nodes, target)

    def test_split_nodes_delimiter2(self):
        node = TextNode("This is text with **bold words**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        target = [
            TextNode("This is text with ", text_type_text),
            TextNode("bold words", text_type_bold),
            TextNode("", text_type_text)
            ]
        self.assertEqual(new_nodes, target)

    def test_split_nodes_delimiter3(self):
        node = TextNode("This *word* is *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        target = [
            TextNode("This ", text_type_text),
            TextNode("word", text_type_italic),
            TextNode(" is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode("", text_type_text)
            ]
        self.assertEqual(new_nodes, target)

    def test_split_nodes_delimiter4(self):
        node = TextNode("**Bold** move", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        target = [
            TextNode("", text_type_text),
            TextNode("Bold", text_type_bold),
            TextNode(" move", text_type_text)
            ]
        self.assertEqual(new_nodes, target)

    def test_split_nodes_image(self):
        nodes = [
            TextNode("This is text with ![an image](path/to/image) in it", text_type_text)
            ]
        target = [
            TextNode("This is text with ", text_type_text),
            TextNode("an image", text_type_image, "path/to/image"),
            TextNode(" in it", text_type_text)
        ]
        self.assertEqual(split_nodes_image(nodes), target)

    def test_split_nodes_image2(self):
        nodes = [
            TextNode(
                "This is text with ![two](path/to/image1) ![images](path/to/image2)", 
                text_type_text
                )
            ]
        target = [
            TextNode("This is text with ", text_type_text),
            TextNode("two", text_type_image, "path/to/image1"),
            TextNode(" ", text_type_text),
            TextNode("images", text_type_image, "path/to/image2")
        ]
        self.assertEqual(split_nodes_image(nodes), target)

    def test_split_nodes_image3(self):
        nodes = [
            TextNode("just text", text_type_text)
            ]
        target = [
            TextNode("just text", text_type_text)
        ]
        self.assertEqual(split_nodes_image(nodes), target)

    def test_split_nodes_image4(self):
        nodes = [
            TextNode("![an image](path/to/image1)", text_type_text)
            ]
        target = [
            TextNode("an image", text_type_image, "path/to/image1"),
        ]
        self.assertEqual(split_nodes_image(nodes), target)

    def test_split_nodes_image5(self):
        nodes = [
            TextNode(
                "This is text with ![two](path/to/image1) ![images](path/to/image2)", 
                text_type_text
                ),
            TextNode("This is text with ![an image](path/to/image) in it", text_type_text)
            ]
        target = [
            TextNode("This is text with ", text_type_text),
            TextNode("two", text_type_image, "path/to/image1"),
            TextNode(" ", text_type_text),
            TextNode("images", text_type_image, "path/to/image2"),
            TextNode("This is text with ", text_type_text),
            TextNode("an image", text_type_image, "path/to/image"),
            TextNode(" in it", text_type_text)
        ]
        self.assertEqual(split_nodes_image(nodes), target)

    def test_split_nodes_link(self):
        nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", 
                text_type_text
                )
        ]
        target = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(split_nodes_link(nodes), target)

    def test_split_nodes_link2(self):
        nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) in the middle", 
                text_type_text
                )
        ]
        target = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" in the middle", text_type_text),
        ]
        self.assertEqual(split_nodes_link(nodes), target)

    def test_split_nodes_link3(self):
        nodes = [
            TextNode("This is just text", text_type_text)
        ]
        target = [
            TextNode("This is just text", text_type_text)
        ]
        self.assertEqual(split_nodes_link(nodes), target)

    def test_split_nodes_link4(self):
        nodes = [
            TextNode("This is just text", text_type_text),
            TextNode("This is text with a [link](https://www.boot.dev)", text_type_text)
        ]
        target = [
            TextNode("This is just text", text_type_text),
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.boot.dev")
        ]
        self.assertEqual(split_nodes_link(nodes), target)

if __name__ == '__main__':
    unittest.main()
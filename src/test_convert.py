import unittest

from convert import *


class TestConvert(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode("raw text", "text")
        target = LeafNode(value="raw text")
        self.assertEqual(text_node_to_html_node(node), target)

    def test_text_node_to_html_node2(self):
        node = TextNode("bold text", "bold")
        target = LeafNode("b", "bold text")
        self.assertEqual(text_node_to_html_node(node), target)

    def test_text_node_to_html_node3(self):
        node = TextNode("italic text", "italic")
        target = LeafNode("i", "italic text")
        self.assertEqual(text_node_to_html_node(node), target)

    def test_text_node_to_html_node4(self):
        node = TextNode("code text", "code")
        target = LeafNode("code", "code text")
        self.assertEqual(text_node_to_html_node(node), target)

    def test_text_node_to_html_node5(self):
        node = TextNode("anchor", "link", "https://www.boot.dev")
        target = LeafNode("a", "anchor", {"href": "https://www.boot.dev"})
        self.assertEqual(text_node_to_html_node(node), target)

    def test_text_node_to_html_node6(self):
        node = TextNode("pixels", "image", "/path/to/image")
        target = LeafNode("img", "", {"src": "/path/to/image", "alt": "pixels"})
        self.assertEqual(text_node_to_html_node(node), target)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        target = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
            ]
        self.assertEqual(text_to_textnodes(text), target)

    def test_text_to_textnodes2(self):
        text = "text"
        target = [
            TextNode("text", text_type_text)
            ]
        self.assertEqual(text_to_textnodes(text), target)

    def test_text_to_textnodes3(self):
        text = "Here's `some code` with *text*"
        target = [
            TextNode("Here's ", text_type_text),
            TextNode("some code", text_type_code),
            TextNode(" with ", text_type_text),
            TextNode("text", text_type_italic)
            ]
        self.assertEqual(text_to_textnodes(text), target)


if __name__ == "__main__":
    unittest.main()
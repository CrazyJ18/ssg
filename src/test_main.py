import unittest

from main import *


class TestMain(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
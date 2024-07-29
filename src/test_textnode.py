import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", "italic", "www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "www.boot.dev")
        self.assertEqual(node, node2)
    def test_eq3(self):
        node = TextNode("", "italic")
        node2 = TextNode("", "italic")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a test node", "bold")
        self.assertNotEqual(node, node2)
    def test_not_eq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    def test_not_eq3(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

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


if __name__ == "__main__":
    unittest.main()
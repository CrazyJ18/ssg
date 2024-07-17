import unittest

from textnode import TextNode


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



if __name__ == "__main__":
    unittest.main()
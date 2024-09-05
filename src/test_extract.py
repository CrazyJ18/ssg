import unittest

from extract import *


class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        target = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        self.assertEqual(extract_markdown_images(text), target)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        target = [
            ("to boot dev", "https://www.boot.dev"), 
            ("to youtube", "https://www.youtube.com/@bootdotdev")
            ]
        self.assertEqual(extract_markdown_links(text), target)

    def test_extract_markdown_links2(self):
        text = "[Here](https://www.google.com) is your link"
        target = [
            ("Here", "https://www.google.com")
            ]
        self.assertEqual(extract_markdown_links(text), target)

    def test_extract_title(self):
        markdown = "# Hello"
        target = "Hello"
        self.assertEqual(extract_title(markdown), target)

    def test_extract_title2(self):
        markdown = "# Hello   "
        target = "Hello"
        self.assertEqual(extract_title(markdown), target)

    def test_extract_title3(self):
        markdown = "Hello   "
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_extract_title4(self):
        markdown = "#    Hello   "
        target = "Hello"
        self.assertEqual(extract_title(markdown), target)


if __name__ == '__main__':
    unittest.main()
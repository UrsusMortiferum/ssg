import unittest

from markdown_parser import split_nodes_delimiter
from textnode import TextNode, TextType


class TextMarkdownParser(unittest.TestCase):
    def test_delimiter_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_double_delimiter(self):
        node = TextNode("**bold** and `code`", TextType.TEXT)
        first_step = split_nodes_delimiter([node], "**", TextType.BOLD)
        second_step = split_nodes_delimiter(first_step, "`", TextType.CODE)
        self.assertListEqual(
            second_step,
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
        )

    def test_delimiter_multiword(self):
        node = TextNode("**bold word word word** word word word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("bold word word word", TextType.BOLD),
                TextNode(" word word word", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()

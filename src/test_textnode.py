import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_func(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTrue(node.__eq__(node2))

    def test_repr(self):
        node = TextNode("Some anchor text", TextType.LINK, "https://www.boot.dev")
        expected_repr = "TextNode(Some anchor text, link, https://www.boot.dev)"
        self.assertEqual(repr(node), expected_repr)

    def test_text_types(self):
        scenarios = ["text", "bold", "italic", "code", "link", "image"]
        for scenario in scenarios:
            text_type = TextType[scenario.upper()]
            node = TextNode(scenario + " text", text_type)
            self.assertEqual(node.text_type, text_type)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_a_node_without_url(self):
        try:
            TextNode("This is a test node", TextType.TEXT)
        except TypeError:
            self.fail("TextNode raised an exception when url was omitted")

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
            repr(node), "TextNode(This is a link node, link, https://www.boot.dev)"
        )

    def test_is_text_node(self):
        node = TextNode("This is a test node", TextType.TEXT)
        self.assertIsInstance(node, TextNode)

    def test_url_is_none(self):
        node = TextNode("This is a test node", TextType.TEXT)
        self.assertIsNone(node.url)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://codeberg.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://codeberg.com"})


if __name__ == "__main__":
    unittest.main()

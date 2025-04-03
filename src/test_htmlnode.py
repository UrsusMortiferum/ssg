import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "test paragraph node",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        expected_repr = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_repr)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "test paragraph node",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        expected_repr = "HTMLNode(tag: p, text: test paragraph node, children: None, props: {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html(self):
        node = HTMLNode(
            "p",
            "test paragraph node",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_eq(self):
        node = HTMLNode(
            "h1",
            "Hello there",
        )
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Hello there")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


if __name__ == "__main__":
    unittest.main()

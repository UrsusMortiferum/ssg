import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, there!")
        self.assertEqual(node.to_html(), "<p>Hello, there!</p>")

    def test_leaf_to_html_a_href(self):
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node2.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_repr(self):
        node = LeafNode(
            "p",
            "test paragraph node",
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            repr(node),
            "LeafNode(tag: p, text: test paragraph node, props: {'href': 'https://www.google.com', 'target': '_blank'})",
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello there!")
        self.assertEqual(node.to_html(), "Hello there!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_parent_repr(self):
        node = ParentNode("span", "child")
        self.assertEqual(
            repr(node), "ParentNode(tag: span, children: child, props: None)"
        )


if __name__ == "__main__":
    unittest.main()

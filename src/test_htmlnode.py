import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a test paragraph node",
            None,
            {
                "href": "https://codeberg.org/",
                "target": "_blank",
            },
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(p, This is a test paragraph node, children: None, {'href': 'https://codeberg.org/', 'target': '_blank'})",
        )

    def test_eq(self):
        node = HTMLNode("p", "text", None, None)
        node2 = HTMLNode("p", "text", None, None)
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = HTMLNode("p", "text", None, None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://codeberg.org/",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://codeberg.org/" target="_blank"'
        )

    def test_is_html_node(self):
        node = HTMLNode(None, None, None, None)
        self.assertIsInstance(node, HTMLNode)


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(repr(node), "LeafNode(p, This is a paragraph, None)")

    def test_props_to_html(self):
        node = LeafNode(
            None,
            None,
            {
                "href": "https://codeberg.org/",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://codeberg.org/" target="_blank"'
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Text, yup", None)
        self.assertEqual(node.to_html(), "Text, yup")

    def test_is_leaf_node(self):
        node = LeafNode("p", "This is a paragraph", None)
        self.assertIsInstance(node, LeafNode)

    def test_eq(self):
        node = LeafNode("p", "This is a paragraph", None)
        node2 = LeafNode("p", "This is a paragraph", None)
        self.assertEqual(node, node2)


class TestParentNode(unittest.TestCase):
    def test_repr(self):
        node = ParentNode("p", [LeafNode("span", "child")])
        self.assertEqual(
            repr(node), "ParentNode(p, children: [LeafNode(span, child, None)], None)"
        )

    def test_to_html_with_children(self):
        node = ParentNode("p", [LeafNode("span", "child")])
        self.assertEqual(node.to_html(), "<p><span>child</span></p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>"
        )


if __name__ == "__main__":
    unittest.main()

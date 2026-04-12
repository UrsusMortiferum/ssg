from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


TYPE_MAP = {
    TextType.TEXT: lambda t: LeafNode(None, t.text),
    TextType.BOLD: lambda t: LeafNode("b", t.text),
    TextType.ITALIC: lambda t: LeafNode("i", t.text),
    TextType.CODE: lambda t: LeafNode("code", t.text),
    TextType.LINK: lambda t: LeafNode("a", t.text, {"href": t.url}),
    TextType.IMAGE: lambda t: LeafNode("img", "", {"src": t.url, "alt": t.text}),
}


def text_node_to_html_node(text_node):
    handler = TYPE_MAP.get(text_node.text_type)
    if handler is None:
        raise ValueError(f"Invalid text type: {text_node.text_type}")
    return handler(text_node)

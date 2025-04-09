from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.extend(old_nodes)
        if old_node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Invalid Markdown syntax, check {delimiter}")

        def extract_text(text, delimiter):
            return text.split(delimiter)[1::2]

        print(extract_text(old_node.text, delimiter))

        # text = old_node.text.split(delimiter, maxsplit=1)
        # text = text[0]
        # print(text)
        # new_node = TextNode(text, TextType.TEXT)
        # new_nodes.extend(new_node)

    # for node in old_nodes:
    #     text = node.text
    #     text = text.split(delimiter)
    #     print(text)

    return new_nodes

    # new_nodes = old_nodes.split(delimiter)
    # print(new_nodes)


node = TextNode("This is text with a `code block` word", TextType.TEXT)
node2 = TextNode(
    "This is text with a `code block` word and another `code block two` word",
    TextType.TEXT,
)
# node2 = TextNode("This is text with a `code block`` word", TextType.TEXT)
# node3 = TextNode("This is text with a `code block` w`ord", TextType.TEXT)
# print(f"node: {node}")
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
new_nodes2 = split_nodes_delimiter([node2], "`", TextType.CODE)
# new_nodes = split_nodes_delimiter([node3], "`", TextType.CODE)
# print(f"new nodes: {new_nodes}")

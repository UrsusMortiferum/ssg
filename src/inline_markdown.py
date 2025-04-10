from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_nodes)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(
                f"Invalid markdown, formatter section not closed, check {delimiter}"
            )
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


node = TextNode("This is text with a `code block` word", TextType.TEXT)
node2 = TextNode(
    "This is text with a `code block` word and another `code block two` word",
    TextType.TEXT,
)
node3 = TextNode("This is text with a `code block`` word", TextType.TEXT)
# node2 = TextNode("This is text with a `code block`` word", TextType.TEXT)
# node3 = TextNode("This is text with a `code block` w`ord", TextType.TEXT)
# print(f"node: {node}")
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
new_nodes2 = split_nodes_delimiter([node2], "`", TextType.CODE)
new_nodes3 = split_nodes_delimiter([node2], "`", TextType.CODE)
print(new_nodes)
print(new_nodes2)
print(new_nodes3)

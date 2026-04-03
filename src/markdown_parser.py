from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            output.append(old_node)
            continue
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception(f"invalid markdown: check {delimiter}")
        split_nodes = []
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        output.extend(split_nodes)
    return output

import re
from textnode import TextType, TextNode


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes)
    nodes = split_nodes_patterns(nodes)
    return nodes


def split_nodes_delimiter(nodes):
    delimiters = [
        ("**", TextType.BOLD),
        ("_", TextType.ITALIC),
        ("`", TextType.CODE),
    ]

    for delimiter, text_type in delimiters:
        new_nodes = []
        for node in nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
            sections = node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception(f"invalid markdown: check {delimiter}")
            for i, section in enumerate(sections):
                if section == "":
                    continue
                node_type = TextType.TEXT if i % 2 == 0 else text_type
                new_nodes.append(TextNode(section, node_type))
        nodes = new_nodes

    return nodes


def split_nodes_patterns(nodes):
    patterns = [
        (r"\!\[(.*?)\]\((.*?)\)", TextType.IMAGE),
        (r"(?<!\!)\[(.*?)\]\((.*?)\)", TextType.LINK),
    ]

    for pattern, node_type in patterns:
        new_nodes = []
        for node in nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
            current_text = node.text
            matches = re.findall(pattern, current_text)
            if not matches:
                new_nodes.append(node)
                continue
            for match_text, match_url in matches:
                delimiter = build_match_marker(match_text, match_url, node_type)
                sections = current_text.split(delimiter, 1)
                if len(sections) != 2:
                    raise ValueError(
                        f"invalid markdown: {node_type} section not closed"
                    )
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(match_text, node_type, match_url))
                current_text = sections[1]
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
        nodes = new_nodes

    return nodes


def build_match_marker(match_text, match_url, node_type):
    delimiter = f"[{match_text}]({match_url})"
    if node_type == TextType.IMAGE:
        return "!" + delimiter
    if node_type == TextType.LINK:
        return delimiter
    raise ValueError(f"invalid node_type: {node_type}")

import re
from textnode import TextType, TextNode


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_image(new_nodes)
    return new_nodes


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


def split_nodes_image(old_nodes):
    output = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            output.append(old_node)
            continue
        text = old_node.text
        matches = extract_markdown_images(old_node.text)
        if len(matches) == 0:
            output.append(old_node)
            continue
        for match in matches:
            delimiter = f"![{match[0]}]({match[1]})"
            sections = text.split(delimiter, 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown: image section not closed")
            if sections[0] != "":
                output.append(TextNode(sections[0], TextType.TEXT))
            output.append(TextNode(match[0], TextType.IMAGE, match[1]))
            text = sections[1]
        if text != "":
            output.append(TextNode(text, TextType.TEXT))
    return output


def split_nodes_link(old_nodes):
    output = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            output.append(old_node)
            continue
        text = old_node.text
        matches = extract_markdown_links(text)
        if len(matches) == 0:
            output.append(old_node)
            continue
        for match in matches:
            delimiter = f"[{match[0]}]({match[1]})"
            sections = text.split(delimiter, 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown: link section not closed")
            if sections[0] != "":
                output.append(TextNode(sections[0], TextType.TEXT))
            output.append(TextNode(match[0], TextType.LINK, match[1]))
            text = sections[1]
        if text != "":
            output.append(TextNode(text, TextType.TEXT))
    return output


def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# debug_helper("text conversion", text_to_textnodes(text))
# [
#     TextNode("This is ", TextType.TEXT),
#     TextNode("text", TextType.BOLD),
#     TextNode(" with an ", TextType.TEXT),
#     TextNode("italic", TextType.ITALIC),
#     TextNode(" word and a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" and an ", TextType.TEXT),
#     TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#     TextNode(" and a ", TextType.TEXT),
#     TextNode("link", TextType.LINK, "https://boot.dev"),
# ]

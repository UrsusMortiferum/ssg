import re
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


def split_nodes_image(old_nodes):
    output = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            output.append(old_node)
            continue
        matches = extract_markdown_images(old_node.text)
        sections = []
        text = old_node.text
        for i in range(len(matches)):
            delimiter = f"![{matches[i][0]}]({matches[i][1]})"
            tmp = text.split(delimiter, 1)
            sections.append(tmp[0])
            sections.append(matches[i])
            text = tmp[1]
        sections.append(text)
        split_nodes = []
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if type(sections[i]) is str:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(
                    TextNode(sections[i][0], TextType.IMAGE, sections[i][1])
                )
        output.extend(split_nodes)
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

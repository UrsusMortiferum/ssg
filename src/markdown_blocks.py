from enum import Enum
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    out = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        out.append(block)
    return out


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    lines = block.split("\n")
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1] == "```":
        return BlockType.CODE
    quoted = list(filter(lambda line: line.startswith(">"), lines))
    if len(quoted) == len(lines):
        return BlockType.QUOTE
    unordered = list(filter(lambda line: line.startswith("- "), lines))
    if len(unordered) == len(lines):
        return BlockType.UNORDERED_LIST
    ordered = False
    for i, line in enumerate(lines):
        if line.startswith(f"{1 + i}. "):
            ordered = True
            continue
        ordered = False
    if ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block):
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            lines = block.split("\n")
            paragraph = " ".join(lines)
            children = text_to_children(paragraph)
            return ParentNode("p", children)
        case BlockType.HEADING:
            level = 0
            for ch in block:
                if ch == "#":
                    level += 1
                else:
                    break
            text = block[level + 1 :]
            children = text_to_children(text)
            return ParentNode(f"h{level}", children)
        case BlockType.CODE:
            text = block[4:-3]  # we extract text between ```\n and ```
            text_node = TextNode(text, TextType.TEXT)
            child_node = text_node_to_html_node(text_node)
            return ParentNode("pre", [ParentNode("code", [child_node])])
        case BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = [line.lstrip(">").strip() for line in lines]
            quote = " ".join(cleaned_lines)
            children = text_to_children(quote)
            return ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            items = block.split("\n")
            html_nodes = []
            for item in items:
                children = text_to_children(item[2:])
                html_nodes.append(ParentNode("li", children))
            return ParentNode("ul", html_nodes)
        case BlockType.ORDERED_LIST:
            items = block.split("\n")
            html_nodes = []
            for item in items:
                children = text_to_children(item.split(". ", 1)[1])
                html_nodes.append(ParentNode("li", children))
            return ParentNode("ol", html_nodes)
        case _:
            raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

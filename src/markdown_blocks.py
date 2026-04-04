from enum import Enum


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

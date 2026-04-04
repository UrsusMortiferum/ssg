import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        text = """
Paragraph

# Heading

```
Code
```

> Quote
>Quote

- Unordered list
- Unordered list

1. Ordered list
2. Ordered list

1. Paragraph
3. Paragraph

-Paragraph
- Paragraph

```paragraph```
"""
        blocks = markdown_to_blocks(text)
        types = [block_to_block_type(b) for b in blocks]
        self.assertListEqual(
            types,
            [
                BlockType.PARAGRAPH,
                BlockType.HEADING,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.UNORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
        )

    def test_block_to_block_type_paragraph(self):
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        block = "## heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    # def test_block_to_block_type_not_code(self):
    #     block = "```code\n```"
    #     self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_not_code_alt(self):
        block = "```\ncode```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

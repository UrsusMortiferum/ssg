import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node,
)


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

    def test_headings_1(self):
        md = "# Heading 1"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Heading 1</h1></div>")

    def test_headings_2(self):
        md = "## Heading 2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h2>Heading 2</h2></div>")

    def test_headings_3(self):
        md = "### Heading 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h3>Heading 3</h3></div>")

    def test_headings_4(self):
        md = "#### Heading 4"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h4>Heading 4</h4></div>")

    def test_headings_5(self):
        md = "##### Heading 5"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h5>Heading 5</h5></div>")

    def test_headings_6(self):
        md = "###### Heading 6"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h6>Heading 6</h6></div>")

    def test_paragraphs(self):
        md = """This is a simple paragraph with no inline formatting at all.

This is a paragraph with **bold text**, _italic text_, `inline code`, and even an ![image](https://example.com/img.png) and a [link](https://boot.dev) all in one line.

Multiple lines in
a single paragraph
should be joined with spaces.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><p>This is a simple paragraph with no inline formatting at all.</p><p>This is a paragraph with <b>bold text</b>, <i>italic text</i>, <code>inline code</code>, and even an <img src="https://example.com/img.png" alt="image"> and a <a href="https://boot.dev">link</a> all in one line.</p><p>Multiple lines in a single paragraph should be joined with spaces.</p></div>""",
        )

    def test_unorder_list(self):
        md = """- Simple unordered item
- Item with **bold** word
- Item with _italic_ and `code`
- Item with a [link](https://example.com)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><ul><li>Simple unordered item</li><li>Item with <b>bold</b> word</li><li>Item with <i>italic</i> and <code>code</code></li><li>Item with a <a href="https://example.com">link</a></li></ul></div>""",
        )

    def test_ordered_list(self):
        md = """1. First ordered item
2. Second with **bold**
3. Third with _italic_ and `code`
4. Fourth with a [link](https://example.com)
5. Fifth plain item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><ol><li>First ordered item</li><li>Second with <b>bold</b></li><li>Third with <i>italic</i> and <code>code</code></li><li>Fourth with a <a href="https://example.com">link</a></li><li>Fifth plain item</li></ol></div>""",
        )

    def test_quotes(self):
        md = """> A single line quote

> A multiline quote
> with **bold** and _italic_
> and even `code` inside
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><blockquote>A single line quote</blockquote><blockquote>A multiline quote with <b>bold</b> and <i>italic</i> and even <code>code</code> inside</blockquote></div>""",
        )

    def test_code(self):
        md = """```
This is a code block
with asterisks and underscores
and [brackets](that should not parse)
all left completely raw
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><pre><code>This is a code block
with asterisks and underscores
and [brackets](that should not parse)
all left completely raw
</code></pre></div>""",
        )


if __name__ == "__main__":
    unittest.main()

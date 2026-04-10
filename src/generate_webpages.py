import os
from copy_dir_contents import establish_project_dir
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Where's my title babe? aka no title found")


def generate_page(src_path, template_path):
    project_dir = establish_project_dir()
    dst_path = src_path.replace("content", "public").replace(".md", ".html")
    print(f"Generating web page from {src_path} to {dst_path} using {template_path}.")

    abs_src_path = os.path.join(project_dir, src_path)
    abs_template_path = os.path.join(project_dir, template_path)
    abs_dst_path = os.path.join(project_dir, dst_path)
    abs_dst_dir = os.path.dirname(abs_dst_path)
    os.makedirs(abs_dst_dir, exist_ok=True)  # for entries directly in public

    with open(abs_src_path, "r") as f:
        markdown = f.read()

    with open(abs_template_path, "r") as f:
        html_template = f.read()

    title = extract_title(markdown)
    node = markdown_to_html_node(markdown)
    html = node.to_html()

    html_output = html_template.replace("{{ Title }}", title)
    html_output = html_output.replace("{{ Content }}", html)

    with open(abs_dst_path, "x") as f:
        f.write(html_output)

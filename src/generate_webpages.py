import os
from copy_dir_contents import establish_project_dir
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Where's my title babe? aka no title found")


def populate_template(template, markdown, basepath):
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()
    html = html.replace('href="/', f'href"{basepath}').replace(
        'src="/', f'src"{basepath}'
    )
    return template.replace("{{ Title }}", title).replace("{{ Content }}", html)


def generate_pages(content_dir, template_path, dst_dir, basepath, _cache={}):
    if "project_dir" not in _cache:
        _cache["project_dir"] = establish_project_dir()
    project_dir = _cache["project_dir"]
    if "template" not in _cache:
        abs_template_path = os.path.join(project_dir, template_path)
        with open(abs_template_path, "r") as f:
            _cache["template"] = f.read()
    template = _cache["template"]

    abs_src_dir = os.path.join(project_dir, content_dir)
    abs_dst_dir = os.path.join(project_dir, dst_dir)
    entries = os.listdir(abs_src_dir)
    for entry in entries:
        entry_path = os.path.join(abs_src_dir, entry)
        if os.path.isfile(entry_path):
            with open(entry_path, "r") as f:
                markdown = f.read()
            html_output = populate_template(template, markdown, basepath)
            abs_dst_path = os.path.join(abs_dst_dir, entry).replace(".md", ".html")
            with open(abs_dst_path, "w") as f:
                f.write(html_output)
        else:
            next_content_dir = os.path.join(content_dir, entry)
            next_dst_dir = os.path.join(dst_dir, entry)
            next_abs_dst_dir = os.path.join(abs_dst_dir, entry)
            os.makedirs(next_abs_dst_dir)
            # os.makedirs(abs_dst_dir, exist_ok=True)  # for entries directly in public
            generate_pages(next_content_dir, template_path, next_dst_dir, basepath)

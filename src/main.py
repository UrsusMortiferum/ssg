import sys

from copy_dir_contents import prepare_dst_dir
from generate_webpages import generate_pages

content_dir = "content"
template_path = "template.html"
dst_dir = "docs"

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


def main():
    prepare_dst_dir(dst_dir)
    generate_pages(content_dir, template_path, dst_dir, basepath)


if __name__ == "__main__":
    main()

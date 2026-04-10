from copy_dir_contents import prepare_public_dir
from generate_webpages import generate_pages

content_dir = "content"
template_path = "template.html"
dst_dir = "public"


def main():
    prepare_public_dir()
    generate_pages(content_dir, template_path, dst_dir)


if __name__ == "__main__":
    main()

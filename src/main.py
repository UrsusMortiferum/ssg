from copy_dir_contents import prepare_public_dir
from generate_webpages import generate_page

src_path = "content/index.md"
template_path = "template.html"


def main():
    prepare_public_dir()
    generate_page(src_path, template_path)


if __name__ == "__main__":
    main()

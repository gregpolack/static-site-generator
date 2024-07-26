from copystatic import copy_from_source
from generate_page import generate_pages_recursive

static_path = "./static/"
public_path = "./public/"
content_path = "./content/"
template_path = "./template.html"

def main():
    copy_from_source(static_path, public_path)

    generate_pages_recursive(content_path, template_path, public_path )

if __name__ == "__main__":
    main()
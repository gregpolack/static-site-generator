from copystatic import copy_from_source
from generate_page import generate_page

src = "./static/"
dst = "./public/"

def main():
    copy_from_source(src, dst)

    generate_page("./content/index.md", "./template.html", "./public/index.html")
    
if __name__ == "__main__":
    main()
from copystatic import copy_from_source

src = "./static/"
dst = "./public/"

def main():
    copy_from_source(src, dst)

if __name__ == "__main__":
    main()
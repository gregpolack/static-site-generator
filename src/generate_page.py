from blocks import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    content = path_to_variable(from_path)
    template = path_to_variable(template_path)
 
    node = markdown_to_html_node(content)
    html_text = node.to_html()

    page_title = extract_title(content)

    template = template.replace(r"{{ Title }}", page_title)
    template = template.replace(r"{{ Content }}", html_text)

    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        filepath = os.path.join(dir_path_content, entry)

        if os.path.isfile(filepath):
            generate_page(filepath, template_path, os.path.join(dest_dir_path, "index.html"))
        else:
            os.mkdir(os.path.join(dest_dir_path, entry))
            generate_pages_recursive(filepath, template_path, os.path.join(dest_dir_path, entry))

def path_to_variable(path):
    f = open(path, "r")
    content = f.read()
    f.close()

    return content

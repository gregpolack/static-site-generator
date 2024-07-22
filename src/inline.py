from textnode import TextNode
import re



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError ("One of the words is missing a closing or opening delimiter.")

        if node.text_type != "text":
            new_nodes.append(node)
        else:
            split_nodes = []
            split_text = node.text.split(delimiter)

            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                if i % 2 != 0:
                    match text_type:
                        case "code":
                            split_nodes.append(TextNode(split_text[i], "code"))
                        case "bold":
                            split_nodes.append(TextNode(split_text[i], "bold"))
                        case "italic":
                            split_nodes.append(TextNode(split_text[i], "italic"))
                        case _:
                            raise ValueError("Unsupported delimiter tag.")
                else:
                    split_nodes.append(TextNode(split_text[i], "text"))
            
            new_nodes.extend(split_nodes)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        nodes = []
        
        images = extract_markdown_images(node.text)
        for image in images:
            nodes.append(TextNode(image[0], "image", image[1]))
        
        sections = re.split(r"!\[.+?\]\(.+?\)", node.text)
        for section in sections:
            if section != "":
                nodes.append(TextNode(section, "text"))

        sorted_nodes = sorted(nodes, key = lambda x: node.text.index(x.text))
        new_nodes.extend(sorted_nodes)
            
    return new_nodes
         

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        nodes = []
        
        links = extract_markdown_links(node.text)
        for link in links:
            nodes.append(TextNode(link[0], "link", link[1]))
        
        sections = re.split(r"\[.+?\]\(.+?\)", node.text)
        for section in sections:
            if section != "":
                nodes.append(TextNode(section, "text"))

        sorted_nodes = sorted(nodes, key = lambda x: node.text.index(x.text))
        new_nodes.extend(sorted_nodes)
            
    return new_nodes
            
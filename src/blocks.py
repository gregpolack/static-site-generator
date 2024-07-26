from htmlnode import ParentNode
from inline import text_to_textnodes
from textnode import text_node_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ").strip()
    
    raise Exception("Markdown has no h1 header")

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    
    stripped_blocks = list(map(lambda x: x.strip(), blocks))
    filtered_blocks = list(filter(lambda x: x != "", stripped_blocks))

    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    heading_prefixes = ["# ", "## ", "### ", "#### ", "##### ", "###### " ]

    if block.startswith(tuple(heading_prefixes)):
        return "heading"
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    return "paragraph"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        node = block_to_html_node(block, block_type)
        children.append(node)
    
    return ParentNode("div", children, None)

def block_to_html_node(block, block_type):
    lines = block.split("\n")
    
    if block_type == "unordered_list":
        tagged_lines = []

        for line in lines:
            if line.startswith("*"):
                tagged_line = line.replace("* ","<li>") + "</li>"
                tagged_lines.append(tagged_line)
            if line.startswith("-"):
                tagged_line = line.replace("- ","<li>") + "</li>"
                tagged_lines.append(tagged_line)
        
        ulist_text = "".join(tagged_lines)
        children = text_to_children(ulist_text)
        
        return ParentNode("ul", children)
    
    if block_type == "ordered_list":
        tagged_lines = []
        i = 1

        for line in lines:
            tagged_line = line.replace(f"{i}. ", "<li>") + "</li>"
            tagged_lines.append(tagged_line)
            i += 1
        
        olist_text = "".join(tagged_lines)
        children = text_to_children(olist_text)

        return ParentNode("ol", children)

    if block_type == "quote":
        cleared_lines = list(map(lambda x: x.strip(">").strip(), lines))
        quote_text = " ".join(cleared_lines)
        children = text_to_children(quote_text)

        return ParentNode("blockquote", children)
    
    if block_type == "heading":
        phrases = block.split()
        heading_text = block.strip(phrases[0] + " ")
        children = text_to_children(heading_text)

        return ParentNode("h" + str(phrases[0].count("#")), children)
    
    if block_type == "paragraph":
        paragraph = " ".join(lines)
        children = text_to_children(paragraph)

        return ParentNode("p", children)

    if block_type == "code":
        del lines[0]
        del lines[-1]

        code_text = "<pre>" + " ".join(lines) + "</pre>"
        children = text_to_children(code_text)

        return ParentNode("code", children)
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
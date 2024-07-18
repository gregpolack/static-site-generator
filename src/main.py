from htmlnode import *
from textnode import *

def main():
    node = TextNode("This is a text node", "text", "https://boot.dev")
    text_node_to_html_node(node)

def text_node_to_html_node(text_node):
    print(f"text_node.text_type: {text_node.text_type}")
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "b":
            return LeafNode("b", text_node.text)
        case _:
            raise ValueError(f"Unhandled text type: {text_node.text_type}")

if __name__ == "__main__":
    main()
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError ("Leaf node must have a value")
        super().__init__(tag, value, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError ("Leaf node must have a value")
        if self.tag is None:
            return f"{self.value}"
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
        

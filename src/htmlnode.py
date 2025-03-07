class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("to html() must be implemented by subclasses")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children={len(self.children)}, props={self.props})'
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props =None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode(tag="{self.tag}", value="{self.value}", props={self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("Parent node must have a tag.")
        if not children:
            raise ValueError("ParentNode must have at least one child.")
        super().__init__(tag =tag, children = children, props = props)

    def to_html(self):
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
    def __repr__(self):
        return f'ParentNode(tag="{self.tag}", children={len(self.children)}, props={self.props})'
    

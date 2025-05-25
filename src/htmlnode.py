class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html is not implemented")
    
    def props_to_html(self):
        result = ''
        if self.props is None:
            return result
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Value must be provided for LeafNode")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag must be defined for a LeafNode")
        if self.children is None:
            raise ValueError("LeafNode must have at least one child node")
        
        result = f'<{self.tag}{self.props_to_html()}>'
        for node in self.children:
            result += node.to_html()
        result += f'</{self.tag}>'
        return result
    
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
    
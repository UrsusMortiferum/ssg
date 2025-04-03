class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for tag, link in self.props.items():
            props_html += f' {tag}="{link}"'
        return props_html

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, text: {self.value}, children: {self.children}, props: {self.props})"

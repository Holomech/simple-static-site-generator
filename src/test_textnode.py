import unittest
from textnode import TextType, TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("A text node", TextType.BOLD)
        node2 = TextNode("A text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("A text node", TextType.BOLD)
        node2 = TextNode("A text node", TextType.ITALIC)
        node3 = TextNode("text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)

    def test_repr(self):
        node = TextNode("A text node", TextType.BOLD)
        node_repr = node.__repr__()
        node_repr_expected = "TextNode(A text node, bold, None)"
        self.assertEqual(node_repr, node_repr_expected)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
        


if __name__ == "__main__":
    unittest.main()

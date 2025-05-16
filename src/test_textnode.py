import unittest
from textnode import TextType, TextNode

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
        


if __name__ == "__main__":
    unittest.main()

import unittest
from htmlnode import ParentNode, LeafNode

class testParentNode(unittest.TestCase):

    def test_ParentNode_requires_tag(self):
        with self.assertRaises (ValueError):
            ParentNode(None,[LeafNode("b", "Bold text")])
    
    def test_ParentNode_requires_children(self):
        with self.assertRaises (ValueError):
            ParentNode("div",[])

    def test_ParentNode_single_child(self):
        node = ParentNode("p", [LeafNode("b", "Bold text")])
        self.assertEqual(node.to_html(),"<p><b>Bold text</b></p>")

    def test_ParentNode_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None,"Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_ParentNodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p",[LeafNode("b", "Bold text")]),
                ParentNode("p",[LeafNode(None, "Normal text")]),
            ],
        )
        self.assertEqual(node.to_html(),"<div><p><b>Bold text</b></p><p>Normal text</p></div>")

if __name__ == "__main__":
    unittest.main()
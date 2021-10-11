import unittest
from LCA import lca
from binaryTree import Node

# Used for testing
bst = Node(11)
bst.insert(6)
bst.insert(4)
bst.insert(5)
bst.insert(8)
bst.insert(10)
bst.insert(19)
bst.insert(17)
bst.insert(43)
bst.insert(31)
bst.insert(49)


class UnitTests(unittest.TestCase):

    def test_lca(self):
        # Test numbers at both sides of root
        self.assertEqual(11, lca(bst, 5, 49))
        # Test two of the same number
        self.assertEqual(10, lca(bst, 10, 10))
        # Test if where one or two of the Nodes do not exist (9)
        self.assertEqual(None, lca(bst, 6, 9))
        self.assertEqual(None, lca(bst, 48, 2))
        # Test if one number is a direct descendant of the other
        self.assertEqual(19, lca(bst, 49, 19))
        self.assertEqual(6, lca(bst, 5, 6))
        # Test with invalid inputs, eg. Strings & floats
        self.assertEqual(None, lca(bst, "TEST", 19))
        self.assertEqual(None, lca(bst, 1.923, 20))

    def test_bst(self):
        # Test printing
        self.assertEqual("11 (6 (4 (None, 5), 8 (None, 10)), 19 (17, 43 (31, 49)))", str(bst))
        self.assertEqual("8 (None, 10)", str(bst.left.right))
        # Test no input print
        test_bst = Node()
        self.assertEqual("0", str(test_bst))
        # Test negative numbers
        test_bst = Node(3)
        test_bst.insert(-8)
        test_bst.insert(2)
        self.assertEqual("3 (-8 (None, 2), None)", str(test_bst))
        # Test inserting
        test_bst = Node(12)
        self.assertEqual("12", str(test_bst))
        # Adding a a few numbers bigger than the root
        test_bst.insert(13)
        test_bst.insert(16)
        test_bst.insert(29)
        self.assertEqual("12 (None, 13 (None, 16 (None, 29)))", str(test_bst))
        # Test inserting existing node
        test_bst.insert(13)
        self.assertEqual("12 (None, 13 (None, 16 (None, 29)))", str(test_bst))
        # Test inserting with same value as root
        test_bst = Node(65)
        test_bst.insert(65)
        self.assertEqual("65", str(test_bst))
        # Test inserting when root is None
        test_bst = Node(None)
        test_bst.insert(5)
        self.assertEqual("5", str(test_bst))
        # Test invalid inputs
        test_bst = Node("TEST")
        self.assertEqual(None, test_bst.value)
        test_bst = Node(14)
        test_bst.insert("TEST")
        self.assertEqual("14", str(test_bst))
        test_bst.insert(23.6)
        self.assertEqual("14", str(test_bst))
        # Test inserting 0
        test_bst.insert(0)
        self.assertEqual("14 (0, None)", str(test_bst))

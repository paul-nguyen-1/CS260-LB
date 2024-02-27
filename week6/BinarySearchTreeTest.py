import unittest
from BinarySearchTree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def test_add(self):
        tree = BinarySearchTree()

        # Add values to the tree
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        # Test tree structure
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.left.value, 3)
        self.assertEqual(tree.root.right.value, 7)
        self.assertEqual(tree.root.left.left.value, 2)
        self.assertEqual(tree.root.left.right.value, 4)
        self.assertEqual(tree.root.right.left.value, 6)
        self.assertEqual(tree.root.right.right.value, 8)

    def test_remove(self):
        tree = BinarySearchTree()

        # Add values to the tree
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        # Remove nodes from the tree
        tree.remove(2)  # Remove a node with no child
        self.assertEqual(tree.root.left.left, None)

        tree.remove(4)  # Remove a node with one child
        self.assertEqual(tree.root.left.right, None)

        tree.remove(7)  # Remove a node with two children
        self.assertEqual(tree.root.right.value, 8)
        self.assertEqual(tree.root.right.left.value, 6)

        tree.remove(5)  # Remove the root node
        self.assertEqual(tree.root.value, 6)
        self.assertEqual(tree.root.left.value, 3)
        self.assertEqual(tree.root.right.value, 8)

if __name__ == '__main__':
    unittest.main()

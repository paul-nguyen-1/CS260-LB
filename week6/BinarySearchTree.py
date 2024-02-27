class Node:
    def __init__(self, value):
        self.value = value # Node Value
        self.left = None # Left Node (Less than)
        self.right = None # Right Node (Greater than)
        
class BinarySearchTree:
    def __init__(self):
        self.root = None # Root Node

    
    def add(self, value):
        """ Add a node with the given value into the binary search tree
         Args: 
         value: Node value to be added into the subtree 
        """
        new_node = Node(value)
        if not self.root: # initialize root node
            self.root = new_node # assign root node its desired value
            return # return nothing 

        current = self.root # initialize current node
        while current:
            if value <= current.value: # check which side of the subtree to traverse
                if current.left: # check if we can still traverse the left side of the subtree
                    current = current.left # traverse the left side of the current subtree
                else:
                    current.left = new_node # once we get to the end of the left side of the current subtree, add the node value
                    break
            else:
                if current.right: # check if we can still traverse the right side of the subtree
                    current = current.right # traverse the right side of the current subtree
                else:
                    current.right = new_node # once we get to the end of the right side of the current subtree, add the node value
                    break

    def remove(self, value):
        """ Remove node with the given value from the binary search tree.
         Args: 
         value: Node value to be removed from the subtree
        """
        self.root = self.helper_remove(self.root, value) # update the root of the entire tree with the result of helper_remove

    def helper_remove(self, root, value):
        """ Recursive helper function to remove node with the given value from the binary search tree

        Args:
            root: Current root node of the subtree
            value: Node value to be removed from the subtree 

        Returns:
            Updated root of the subtree after the removal.
        """
        if not root:  # check if root node is empty
            return root

        if value < root.value: # check which side of subtree to traverse
            root.left = self.helper_remove(root.left, value) # keep traversing the left side
        elif value > root.value:
            root.right = self.helper_remove(root.right, value) # keep traversing right side
        else:
            # node with only one child or no child
            if not root.left: 
                return root.right # return right node if no left child
            elif not root.right:
                return root.left # return left node if no right child

            # node with two children
            successor_value = self.find_min_value(root.right)  # find the inorder successor
            root.right = self.helper_remove(root.right, successor_value) # remove the node with the inorder successor
            root.value = successor_value  # replace the value of the current root with the inorder successor

        return root # return root node

    def find_min_value(self, root):
        """ Find the minimum value in the subtree rooted at the given node

        Args:
            root: Root node of the subtree

        Returns:
            Minimum value in the subtree
        """
        current = root
        while current.left:
            current = current.left
        return current.value
    
    def inorder(self, root):
        """ In-order Traversal of a binary search tree

        Args:
            root: Root node of the subtree to traverse

        Returns:
            Prints values in-order sequence
            """
        if root:
            if root.left:
                self.inorder(root.left)
            print(root.value, end=' ')
            if root.right:
                self.inorder(root.right)


tree = BinarySearchTree()

# Test inorder traversal
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)
tree.add(8)
tree.inorder(tree.root)
"""
Following tree is getting created:
                     5
                   /   \
                 3      7
                / \    /  \
               2   4  6    8
"""
print('')
tree.remove(7)
tree.remove(4)
tree.inorder(tree.root)

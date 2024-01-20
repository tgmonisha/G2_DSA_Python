class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.val, end=" ")
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.val, end=" ")
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.val, end=" ")

class BinaryTree:
    def __init__(self, root_val, left=None, right=None):
        self.root = Node(root_val, left, right)


# Create a binary tree
tree = BinaryTree(7)
tree.root.left = Node(26)
tree.root.right = Node(31)
tree.root.left.left = Node(12)
tree.root.left.right = Node(55)
tree.root.right.left = Node(61)
tree.root.right.right = Node(37)

# Perform traversals
print("Inorder Traversal:")
tree.root.in_order_traversal()
print("\nPreorder Traversal:")
tree.root.pre_order_traversal()
print("\nPostorder Traversal:")
tree.root.post_order_traversal()


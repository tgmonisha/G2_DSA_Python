class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node:
        print(node.value)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Creating a sample tree
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)

# Preorder Traversal
print("Preorder:")
preorder_traversal(root)


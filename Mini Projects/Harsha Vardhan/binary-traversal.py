class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")


def build_binary_tree():
    key = input("Enter the value for the root node: ")
    root = Node(int(key))
    build_tree_recursive(root)
    return root


def build_tree_recursive(node, child_type="left"):
    child_key = input(
        f"Enter the value for the {child_type} child of {node.key} (or press Enter to skip): "
    )
    if child_key:
        setattr(node, child_type, Node(int(child_key)))
        build_tree_recursive(getattr(node, child_type), "left")
        build_tree_recursive(getattr(node, child_type), "right")


# Flag to check if the binary tree has been built
tree_built = False

while True:
    if not tree_built:
        root = build_binary_tree()
        tree_built = True

    print("\nTraversal Options:")
    print("1. In-order Traversal")
    print("2. Pre-order Traversal")
    print("3. Post-order Traversal")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        print("In-order Traversal:")
        inorder_traversal(root)
    elif choice == "2":
        print("Pre-order Traversal:")
        preorder_traversal(root)
    elif choice == "3":
        print("Post-order Traversal:")
        postorder_traversal(root)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

# Tree traversal in Python


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
        
def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')

def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(50)
root.left = Node(40)
root.right = Node(30)
root.left.left = Node(20)
root.left.right = Node(10)
root.right.left = Node(80)
root.right.right= Node(70)

print("Inorder traversal ")
inorder(root)
print("\nPreorder traversal ")
preorder(root)
print("\nPostorder traversal ")
postorder(root)



#sample output
"""Inorder traversal 
20->40->10->50->80->30->70->
Preorder traversal 
50->40->20->10->30->80->70->
Postorder traversal 
20->10->40->80->70->30->50->"""







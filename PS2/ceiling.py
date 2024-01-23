class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BST:
    def __init__(self):
        self.root = None

    def add(self, root, val):
        if root is None:
            root = Node(val)
        elif val < root:
            if root.left is None:
                root.left = Node(val)
            else:
                root.left = self.add(root.left, val)
        elif val > root:
            if root.right is None:
                root.right = Node(val)
            else:
                root.right = self.add(root.right, val)

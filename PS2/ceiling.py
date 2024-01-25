class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BST:
    def __init__(self):
        self.root = None


def add(root, val):
    if root is None:
        return Node(val)
    elif val < root.val:
        root.left = add(root.left, val)
    elif val > root.val:
        root.right = add(root.right, val)
    return root


def inorder_traversal(root):

    result = ''
    if root is not None:
        left_traversal = inorder_traversal(root.left)
        result = left_traversal + '1'
        right_traversal = inorder_traversal(root.right)
        result += right_traversal
    return result


def main():
    n, k = map(int, input().split())

    tree_set = set()

    for i in range(n):
        vals = list(map(int, input().split()))
        bst = BST()

        for val in vals:
            bst.root = add(bst.root, val)

        print(bst)
        result = inorder_traversal(bst.root)
        print(result)
        tree_set.add(result)

    size = len(tree_set)
    return size


if __name__ == "__main__":
    result = main()
    print(result)

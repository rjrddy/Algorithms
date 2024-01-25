# ceiling.py by Raj Reddy for CS 4150 (1/24/24) coded in Python

''' 
defines Node class with left, right, and value properties
'''
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


'''
defines Binary Search Tree class
sets the root to null value at first
'''
class BST:
    def __init__(self):
        self.root = None


'''
add method for a Binary Search Tree with value as a parameter
'''
def add(root, val):

    # creates a node at root
    if root is None:
        return Node(val)

    # otherwise recursivily addes a node on the left side of the root until a proper location is found
    elif val < root.val:
        root.left = add(root.left, val)

    # same is done as above but for larger than root values
    elif val > root.val:
        root.right = add(root.right, val)

    return root


'''
in-order traversal for a Binary Search Tree
takes in a root as its only parameter
returns an a string representation of a left, right, or root traversal
'''
def inorder_traversal(root):
    result = ''
    if root is not None:

        # works recursivily
        left_traversal = inorder_traversal(root.left)
        result += 'L' + left_traversal
        result += 'root'
        right_traversal = inorder_traversal(root.right)
        result += 'R' + right_traversal

    # returns string output
    return result


'''
main method for the implementation to check for the total number of matching outputs
'''
def main():

    # splits first line of input into 2 respective integer values, n and k
    n, k = map(int, input().split())

    # created a set to store our in-order traversal strings which will avoid duplicates
    tree_set = set()

    # traverses through the n to create the BST
    for i in range(n):

        # seperates the values from the lines of inputs into a list and maps accordingly
        vals = list(map(int, input().split()))
        bst = BST()

        # addes values to create new BST
        for val in vals:
            bst.root = add(bst.root, val)

        # takes the stored in-order traversal string and adds it to the set
        result = inorder_traversal(bst.root)
        tree_set.add(result)

    # returns the size of the set
    size = len(tree_set)
    return size


'''
will accept an input for main and print the result
'''
if __name__ == "__main__":
    result = main()
    print(result)

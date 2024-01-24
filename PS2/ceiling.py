class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BST:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            return Node(val)
        elif val < self.root.val:
            if self.root.left is None:
                self.root.left = Node(val)
            else:
                self.root.left = self.add(self.root.left, val)
        elif val > self.root.val:
            if self.root.right is None:
                self.root.right = Node(val)
            else:
                self.root.right = self.add(self.root.right, val)
        return self.root;
    
    def inorder(self):
        
        arr = []
        
        if self.root is None:
            arr.extend(self.inorder(self.root.left))
            arr.append(self.root)
            arr.extend(self.inorder(self.root.right))
        
        return arr
            
                
def main():
    n, k = map(int, input().split())
    
    for i in range(n):
        
        vals = []
        vals = input().split()
        bst = BST();
       
        for val in vals:
            bst.add(val)
    
    
        

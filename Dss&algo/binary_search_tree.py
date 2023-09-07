# Python program to demonstrate
# insert operation in binary search tree


# A utility class that represents
# an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    node = Node(key)
    if root == None:
        return node
    prev = None
    temp = root
    while temp != None:
        prev = temp
        if temp.val > key:
            temp = temp.left
        elif temp.val < key:
            temp = temp.right
        else:
            return
    if prev.val > key:
        prev.left = node
    else:
        prev.right = node

def findheightoftree(root):
    if root is None:
        return 0
    else:
        l_depth = findheightoftree(root.left)
        r_depth = findheightoftree(root.right)
        
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1

if __name__ == '__main__':
    r = Node(5)
    insert(r, 4)
    insert(r, 10)
    insert(r, 50)
    print(findheightoftree(r))
    

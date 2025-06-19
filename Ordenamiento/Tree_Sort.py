class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def in_order_traversal(root, arr):
    if root:
        in_order_traversal(root.left, arr)
        arr.append(root.val)
        in_order_traversal(root.right, arr)

def tree_sort(arr):
    if len(arr) == 0:
        return arr
    root = None
    for item in arr:
        root = insert(root, item)
    sorted_arr = []
    in_order_traversal(root, sorted_arr)
    return sorted_arr
#developer : Mitesh Chakma
#contact : miteshchakma@gmail.com

import time


start = time.time()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def lca(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = lca(root.left, n1, n2)
    right_lca = lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca

if __name__ == '__main__':
    time.sleep(1)

    end = time.time()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    print("LCA(6,7) = ", lca(root, 6, 7).key)

    print("LCA(3,7) = ", lca(root, 3, 7).key)
    print(f"Runtime of the program is {end - start}")

#Holly Mcevoy 19334633 some of this code is taken from stack overflow and geeksforgeeks
from binaryTree import is_valid_node


def lca(node, a, b):
    if is_valid_node(node, a) and is_valid_node(node, b):
        while node:
            if a < node.value < b:
                return node.value
            elif a == node.value:
                return a
            elif b == node.value:
                return b
            elif min(a, b) < node.value:
                node = node.left
            elif max(a, b) > node.value:
                node = node.right
    return None

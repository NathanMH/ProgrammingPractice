"""####################
Author: Nathan Mador-House
Title: BinaryTree
####################"""

#######################
"""####################
Index:
1. Imports and Readme
2. Functions
3. Main
4. Testing
####################"""
#######################

###################################################################
# 1. Imports and Readme
###################################################################
"""####################
Implementation of a binary tree
####################"""

###################################################################
# 2. Functions
###################################################################

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    # Add item 
    def add_value(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add_value(val, self.root)

    def _add_value(self, val, node):
        if val < node.value:
            if node.left != None:
                self._add_value(val, node.left) 
            else:
                node.left = Node(val)
        else:
            if node.right != None:
                self._add_value(val, node.right)
            else:
                node.right = Node(val)

    def find_value(self, val):
        if self.root != None:
            self._find_value(val, self.root)
        else:
            return node

    def _find_value(self, val, node):
        if val == node.value:
            return node
        elif val < node.value and node.left != None:
            self._find_value(val, node.left)
        elif val > node.value and node.right != None:
            self._find_value(val, node.right)

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node != None:
            self._print_tree(node.left)
            print(str(node.value))
            self._print_tree(node.right)

def make_tree(array):
    tree = Tree()
    for i in array:
        tree.add_value(i)
    return tree

###################################################################
# 3. Main
###################################################################

def tree(array):
    return make_tree(array)

###################################################################
# 4. Testing
###################################################################

test_numbers = [7, 12, 48, 53, 85, 97, 101, 133, 154]

test_tree = tree(test_numbers)
test_tree.print_tree()

print("-------------------")

test_tree.add_value(17)
test_tree.print_tree()

print("-------------------")

test_find = test_tree.find_value(12)
print(test_find)









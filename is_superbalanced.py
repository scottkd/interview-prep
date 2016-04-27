"""Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up).
A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_superbalanced(root):
    level = 1
    max_depth = None
    min_depth = None
    queue = []
    queue.append((level, root))
    while queue:
        level, node = queue.pop()
        if node.left:
            queue.append((level + 1, node.left))
        if node.right:
            queue.append((level + 1, node.right))

        if not node.left and not node.right:
            if not max_depth or level > max_depth:
                max_depth = level
            if not min_depth or level < min_depth:
                min_depth = level

            if max_depth - min_depth > 1:
                return False

    return True

a = BinaryTreeNode('a')
a.insert_left('b')
c=a.insert_right('c')
d=c.insert_right('d')

assert is_superbalanced(a) == True

d.insert_right('e')

assert is_superbalanced(a) == False

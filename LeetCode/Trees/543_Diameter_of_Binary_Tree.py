"""
Problem : 543. Diameter of Binary Tree
Approach :  Use recursion to find the height of each subtree.
            At every node, calculate left_height + right_height.
            Update the maximum diameter found so far.
            Return the height to the parent node.
            After traversing the whole tree, return the maximum diameter.

"""
class Solution(object):
    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        height(root)
        return self.diameter

"""
Problem : 110. Balanced Binary Tree
Approach: Recursively calculate the height of left and right subtrees.
          For each node, check if the height difference is greater than 1.
          If any node is unbalanced, return False.
          Otherwise, return True.
"""
class Solution(object):
    def isBalanced(self, root):

        def height(node):

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1

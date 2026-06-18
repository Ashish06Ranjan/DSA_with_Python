"""

Problem : 104. Maximum Depth of Binary Tree
Approach : If the node is None, return 0. Recursively find the depth of the left subtree.
            Recursively find the depth of the right subtree.
            Return the larger depth plus 1 for the current node.

"""
class Solution(object):
    def maxDepth(self, root):

        if root == None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

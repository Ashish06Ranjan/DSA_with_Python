"""
Problem : 101. Symmetric Approach 
Approach : Compare the left and right subtrees.
            If both nodes are None, return True.
            If one is None and the other isn't, return False.
            Check if the node values are equal. Recursively compare:
            left subtree's left node with right subtree's right node
            left subtree's right node with right subtree's left node
            If all comparisons match, the tree is symmetric.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):

        def mirror(left, right):

            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)
        

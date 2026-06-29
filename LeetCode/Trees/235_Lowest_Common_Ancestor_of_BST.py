"""
Problem : 235. Lowest Common Ancestor of a Binary Search Tree
Approach :  Start from the root of the BST.
            If both p and q are smaller than the current node, move to the left subtree.
            If both are greater than the current node, move to the right subtree.
            Otherwise, the current node is the Lowest Common Ancestor, so return it.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

      while root:
        if p.val<root.val and q.val<root.val:
          root=root.left
        elif p.val>root.val and q.val>root.val:
          root=root.right
        else:
          return root 

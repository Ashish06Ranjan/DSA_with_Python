"""
Problem : 226. Invert Binary Tree
Approach : If the current node is None, return it. Swap the left and right child of the current node.
          Recursively invert the left subtree. Recursively invert the right subtree.
          Return the root of the inverted tree.
"""

class Solution(object):
    def invertTree(self, root):
        
        if root == None:
            return None
        
        # Swap left and right child
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Invert left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

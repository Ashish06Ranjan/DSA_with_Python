"""

Problem : 100 Same Tree
Approach :  Start from the root, compare each pair of nodes, and recursively check their left and right children.
            If the structure and values match at every position, the trees are the same.

"""

class Solution:
    def isSameTree(self, p, q):

        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        if p.val != q.val:
            return False
            
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right

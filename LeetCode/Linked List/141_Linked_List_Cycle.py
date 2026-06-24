"""
Problem : 141. Linked List Cycle
Approach :  Initialise two pointers slow and fast 
            Move the slow by one and the fast by two nodes
            If they meet then the cycle exists 
            and if fast reaches the end then the cycle doesn't exists

"""

class Solution(object):
    def hasCycle(self, head):

      slow = head
      fast = head
      
      while fast and fast.next:

        slow = slow.next
        fast = fast.next.next
        if slow == fast:
          return True 
      return False
        

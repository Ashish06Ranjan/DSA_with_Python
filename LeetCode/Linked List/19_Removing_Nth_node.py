"""
Problem : 19. Remove Nth Node From End of List
Approach :  Create a dummy node before the head.
            Place both slow and fast at the dummy node.
            Move fast ahead by n + 1 steps.
            Move both pointers together until fast reaches the end.
            slow will be just before the node to remove.
            Skip the target node using slow.next = slow.next.next.
            Return dummy.next.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
      dummy = ListNode(0)
      dummy.next = head

      slow = dummy 
      fast = dummy 

      for i in range(n+1):
        fast = fast.next
      while fast:
        slow = slow.next 
        fast = fast.next
      slow.next = slow.next.next
      return dummy.next
      

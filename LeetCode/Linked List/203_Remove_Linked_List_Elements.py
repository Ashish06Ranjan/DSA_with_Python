"""

Problem : 203. Remove Linked List Elements
Approach : Create a dummy → Traverse the list → Skip nodes with the target value → Return the new head.

"""
class Solution(object):
    def removeElements(self, head, val):

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next:

            if current.next.val == val:
                current.next = current.next.next

            else:
                current = current.next

        return dummy.next

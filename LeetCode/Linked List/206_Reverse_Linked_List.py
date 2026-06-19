"""
Problem : 206.Reverse Linked List
Approach : Use two pointers: prev and curr.
            Traverse the linked list.
            For each node, store the next node.
            Reverse the current node's pointer to point to prev.
            Move both pointers one step forward.
            When traversal ends, prev will be the new head of the reversed list.

"""
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:

            next_node = curr.next
            curr.next = prev
            prev = curr

            curr = next_node

        return prev
        

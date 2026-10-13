# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        n_from_start = N - n
        if n_from_start == 0:
            return head.next

        curr = head
        while n_from_start > 1:
            curr = curr.next
            n_from_start -= 1
        
        curr.next = curr.next.next
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr_node = head
        carry = 0
        while l1 and l2:
            curr = l1.val + l2.val + carry
            if curr > 9:
                curr_node.val = curr % 10
                carry = 1
            else:
                curr_node.val = curr
                carry = 0
            if l1.next or l2.next:
                curr_node.next = ListNode()
                curr_node = curr_node.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr = l1.val + carry
            if curr > 9:
                curr_node.val = curr % 10
                carry = 1
            else:
                curr_node.val = curr
                carry = 0
            if l1.next:
                curr_node.next = ListNode()
                curr_node = curr_node.next
            l1 = l1.next
        
        while l2:
            curr = l2.val + carry
            if curr > 9:
                curr_node.val = curr % 10
                carry = 1
            else:
                curr_node.val = curr
                carry = 0
            if l2.next:
                curr_node.next = ListNode()
                curr_node = curr_node.next
            l2 = l2.next

        if carry != 0:
            curr_node.next = ListNode(carry)

        return head

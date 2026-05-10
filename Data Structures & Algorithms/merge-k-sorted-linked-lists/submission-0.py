# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyHead = ListNode()
        curr = dummyHead
        currMin = 0
        k = len(lists)
        while k > 0:
            for i in range(len(lists)):
                if lists[i] and lists[currMin] and lists[i].val < lists[currMin].val:
                    currMin = i
                elif lists[i] and not lists[currMin]:
                    currMin = i
            curr.next = lists[currMin]
            curr = curr.next
            lists[currMin] = lists[currMin].next
            if lists[currMin] == None:
                k -= 1
        return dummyHead.next
            
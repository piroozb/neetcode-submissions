class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        if not curr:
            return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        if self.head:
            tmp = self.head
            self.head = Node(val)
            self.head.next = tmp
        else:
            self.head = Node(val)
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        if self.tail:
            tmp = self.tail
            self.tail = Node(val)
            tmp.next = self.tail
        else:
            self.tail = Node(val)
            self.head = self.tail

    def remove(self, index: int) -> bool:
        if index == 0 and self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            return True
        curr = self.head
        i = 0
        while i < index - 1 and curr:
            curr = curr.next
            i += 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst

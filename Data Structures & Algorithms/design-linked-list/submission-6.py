class MyLinkedList:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0: 
            return -1

        cur = self.head
        while cur:
            if index == 0: 
                return cur.val
            cur = cur.next
            index -= 1

    def addAtHead(self, val: int) -> None:
        newHead = self.ListNode(val) 
        newHead.next = self.head
        self.head = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = self.ListNode(val)
            return

        newTail = self.ListNode(val) 
        cur = self.head
        
        while cur.next:
            cur = cur.next
        
        cur.next = newTail
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index < 0 or index > self.size:
            return

        cur = self.head

        while cur: 
            if index == 1: 
                temp = cur.next
                cur.next = self.ListNode(val, temp)
                self.size += 1
                return

            cur = cur.next
            index -= 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        cur = self.head
        for _ in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
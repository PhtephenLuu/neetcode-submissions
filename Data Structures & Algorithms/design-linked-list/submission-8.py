class MyLinkedList:
    class ListNode:
        def __init__(self, val, next=None):
            self.val = val 
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 
        
        currentIndex = 0
        cur = self.head

        while currentIndex != index: 
            cur = cur.next
            currentIndex += 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = self.ListNode(val)
            self.size += 1
            return

        newHead = self.ListNode(val, self.head)
        self.head = newHead
        self.size += 1


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = self.ListNode(val)

        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: 
            return

        if index == self.size: 
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        
        curInd = 0
        cur = self.head

        while curInd != index - 1:
            cur = cur.next 
            curInd += 1
        
        temp = cur.next 
        cur.next = self.ListNode(val)
        cur.next.next = temp

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or not self.head:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        curInd = 0 
        cur = self.head

        while curInd != index - 1:
            cur = cur.next
            curInd += 1 
        
        cur.next = cur.next.next
        self.size -= 1

'''
Valid indices: 
1. Index > 0 
2. Index < size of list

Edge cases:
Get 
    if the index < 0 or >= size of list 
    traverse linked list to specified index and get val
addAtHead
    if list is empty create new listnode as head
    if not we create a dummy node with the value and then set the next to head and set the dummy node as the head
addAtTail
    if list is empty create new listnode as head we can reuse addAtHead
    traverse until the next pointer of the current node is null. That means we'll be at the last node
    set the next node to a new list node with the value 
addAtUbdex 
    if index == length then add at tail 
    if index > length then do nothing
    if index == 0 then add at head

    traverse list keep track of what element we're on with a counter 
    when the counter is one less than the index create a dummy node with the value
    set the current next pointer to dummy and the dummy next pointer to the original next
deleteAtIndex
    check for valid indices
    traverse linked list until indexth node by keeping track of a counter 
    when it's one off the index then we do the following set current next equal to current next next
    effectively wiping the node

We need helper class for listnode it needs 
1. Value field for the value
2. next pointer to the next node 

for the linked list we need to fields 
1. A head pointer 
2. The size 



'''


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        [0,1,2,3]
        head = 0
        head = 3
        0 <- 1 <- 2 <- 3


        Example 1
        0 <- 1 <- 2 <- 3
        prev = 3
        tempNext = null
        cur = null
        cur.next = null 
        head = 3

        1. Start at the head
        2. Make a temp variable to hold current next reference 
        3. Store current previous node reference which at the start is just the head 
        4. If the current node is the head then set next to null, otherwise set it to previous.
        5. Go to the next node while current node is not null and then set previous to tempNext and repeat step 3-5
        '''

        cur = head
        prev = None
        res = []

        while cur:    
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext
        
        return prev
        


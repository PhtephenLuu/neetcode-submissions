# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Initial thoughts
        - We can simply traverse both linked lists collect both elements into an array
          then sort the array and create a new linked list based off the elements there

        Better solution
        - Iterate over both linked lists at the same time
        - determin the min(list1 current node val, list 2 current node val) this determines 
        - Set value equal to the minimum value, and then set next to a new ListNode(0, None) and go to that new listNode
        - For the node that contained the value that was picked, go to the next node.
        - Repeat above steps until both nodes have been iterated over

        Things to consider:
        - What happens when there's a tie which list do we prioritize. - Assume right
        - Are lists guaranteed to be the same size? - no can have differing sizes
        - Are empty inputs allowed - yes
        - Are we guaranteed to only have valid inputs - yes

        Input: list1 = [1,2,4], list2 = [1,3,5]

        Output: [1,1,2,3,4,5]
        """

        dummy = node = ListNode()
        firstListPointer = list1
        secondListPointer = list2
        

        while firstListPointer and secondListPointer:
            if firstListPointer.val < secondListPointer.val:
                node.next = firstListPointer
                firstListPointer = firstListPointer.next
            else:
                node.next = secondListPointer
                secondListPointer = secondListPointer.next        
            node = node.next
            
        node.next = firstListPointer or secondListPointer

        return dummy.next


        
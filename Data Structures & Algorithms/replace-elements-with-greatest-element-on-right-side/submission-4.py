class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        Last element has to be -1 
        
        currentMaximum = last element = 2
        [2,4,5,3,1,2]
        set last element = -1
        [2,4,5,3,1,-1]
        start looping back from 2nd last element and compare with the currentMax
        [2,4,5,3,2,-1], currMax = 2, 1 < 2 
        [2,4,5,2,2,-1], currMax = 3, 3 > 2
        [2,4,3,2,2,-1], currMax = 5, 5 > 3
        [2,5,3,2,2,-1], currMax = 5, 4 < 5
        [5,5,5,2,2,-1] 
        '''

        # Set currrent max to last element 
        currMax = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)- 2, -1, -1):
            temp = arr[i]
            arr[i] = currMax

            currMax = max(currMax, temp)        
        return arr


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k

        '''
        Input: nums = [3,2,2,3], val = 3
        Output: k = 2, nums = [2,2,_,_]

        nums[3,2,2,3], k = 1
        nums[2,2,2,2]

        Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: k = 5, nums = [0,1,3,0,4,_,_,_]
        
        nums[0,1,2,2,3,0,4,2] k = 5
        nums[0,1,3,0,4,0,4,2]
        '''


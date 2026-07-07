class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        Initialize ans to be [0] * 2n where n = length of nums
        for i in range(lens(ans))
         if i < length of nums 
            ans[i] = nums[i] 
         else: 
            ans[i] = nums[i % n]

        intitial n = 4
        ans length = 8 
        i < 4 is false so we do ans[i] = nums[i % n] 4 / 4 rem 0, 4 % 4 = 0

        Example 
        Input: nums = [1,4,1,2]

        Output: [1,4,1,2,1,4,1,2]

        n = 4
        ans = [0,0,0,0...,0] 

        i = 7
        i % n = 3
        ans[1,4,1,2,1,4,1,2]
        '''

        n = len(nums)
        ans = [0] * 2 * n

        for i in range(len(ans)):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i % n]
        
        return ans



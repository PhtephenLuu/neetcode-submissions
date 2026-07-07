class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSum = [0] * n
        suffixSum = [0] * n
        res = [0] * n

        prefixSum[0] = suffixSum[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            prefixSum[i] = nums[i - 1] * prefixSum[i - 1]
        for i in range(len(nums) - 2, -1, -1): 
            suffixSum[i] = nums[i + 1] * suffixSum[i + 1]
        for i in range(len(nums)):
            res[i] = prefixSum[i] * suffixSum[i]
        
        return res
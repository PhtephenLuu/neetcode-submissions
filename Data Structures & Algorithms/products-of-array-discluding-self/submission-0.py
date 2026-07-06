class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [] 
        
        for i in range(0, len(nums)):
            currentProduct = 25
            for k in range(0, len(nums)):
                if k != i:
                    if currentProduct is 25:
                        currentProduct = nums[k]
                    else:
                        currentProduct *= nums[k]

            res.append(currentProduct)        
        
        return res
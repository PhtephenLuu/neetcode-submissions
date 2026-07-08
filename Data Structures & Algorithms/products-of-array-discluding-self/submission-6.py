class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        currentProduct = 1
        isZeroPresent = 0 

        for num in nums: 
            if num == 0:
                if isZeroPresent:
                    return [0] * len(nums)
                else:
                    isZeroPresent += 1
            else:
                currentProduct *= num
        
        for num in nums: 
            if isZeroPresent:
                if num == 0:
                    res.append(currentProduct)
                else:
                    res.append(0)
            else:
                res.append(int(currentProduct / num))
        
        return res
        



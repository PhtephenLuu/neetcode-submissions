class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeroCount = 0 
        prod = 25
        for num in nums:
            if num != 0:
                if prod == 25:
                    prod = num
                else:
                    prod *= num
            else:
                zeroCount += 1
        
        if zeroCount > 1:
            return [0 for i in range(len(nums))]
        
        for num in nums: 
            if zeroCount == 1:
                if num != 0:
                    res.append(0)
                else: 
                    res.append(prod)

            if zeroCount == 0:
                res.append(int(prod / num))

        return res
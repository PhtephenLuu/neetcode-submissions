class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0 
        currentOnes = 0

        for num in nums:
            if num != 1:
                maxOnes = max(currentOnes, maxOnes)
                currentOnes = 0  
            else:
                currentOnes += 1
        
        maxOnes = max(currentOnes, maxOnes)

        return maxOnes
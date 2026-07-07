class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nonValElements = []
        occVal = 0 

        for num in nums:
            if num != val:
                nonValElements.append(num)
            else:
                occVal += 1
        
        for i in range(len(nums)):
            if i < len(nonValElements):
                nums[i] = nonValElements[i]
            else:
                nums[i] = -1
        
        return len(nonValElements)



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

        Output: [1,2,10,20,20,40]

        Merge algo 

        1. Loop while the left array is smaller than the right array to find the starting point to insert the first element of the right array 
        2. Once you find it, insert and shift all the other elements to the right
        3. Profit

        Example:
        [10,20,20,40,0,0]
        [1,2]

        indL , indR = 0 
        1. 10 < 1 = false   indL = 0, indR = 0 
        2. insert 1 at 0         [1,10,20,20,40,0] indL = 1 indR = 1
        3. 10 < 2 = false   indL = 1, indR = 1
        4. insert 2  at 1       [1,2,10,20,20,40,0] indL = 2, indR = 2
        5. indL < 4 indR = 2 = n != < 2 end loop
        """

        nums1[(m):] = nums2
        nums1.sort()
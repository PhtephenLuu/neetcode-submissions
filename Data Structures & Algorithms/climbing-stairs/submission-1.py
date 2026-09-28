class Solution:
    def __init__(self):
        self.lookup = {}

    def climbStairs(self, n: int) -> int:        
        if(n < 1):
            return 0

        if(n == 1):
            return 1
        elif(n == 2):
            return 2
        
        if n in self.lookup:
            return self.lookup[n]
        else:
            self.lookup[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)


        
        return self.lookup[n]
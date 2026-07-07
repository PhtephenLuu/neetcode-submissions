class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = [] 

        for op in operations: 
            if self.isInteger(op):
                res.append(int(op))
            elif op == "+":
                res.append(sum(res[-2:]))
            elif op == "C":
                res.pop() 
            elif op == "D":
                score = res[-1] * 2
                res.append(score)
            
            print(res)
        return sum(res)

    def isInteger(self, digit: str) -> bool:
        try:
            int(digit)
            return True
        except ValueError:
            return False
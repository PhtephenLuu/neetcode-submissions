class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = [] 
        resSum = 0

        for op in operations: 
            if self.isInteger(op):
                res.append(int(op))
                resSum += int(op)
            elif op == "+":
                val = sum(res[-2:])
                res.append(val)
                resSum += val
            elif op == "C":
                resSum -= res[-1]
                res.pop() 
            elif op == "D":
                score = res[-1] * 2
                res.append(score)
                resSum += score
        return resSum

    def isInteger(self, digit: str) -> bool:
        try:
            int(digit)
            return True
        except ValueError:
            return False
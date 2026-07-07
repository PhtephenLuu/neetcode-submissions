class Solution:
    def isValid(self, s: str) -> bool:
        validBrackets = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
        }

        stack = []
        curInd = 0

        for char in s:
            if char in validBrackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char != validBrackets[stack[-1]]:
                    return False
                else:
                    stack.pop()
                
        return len(stack) == 0

        '''
        whileCurInd < len(s) - 1
        curInd = 0
        '[]'
        ['[', ']']
        stack.pop() = ']' 
        check that stack(curInd) = validBrackets[stack.pop]
        if yes
            curInd++ 
        else:
            return False 
        '''
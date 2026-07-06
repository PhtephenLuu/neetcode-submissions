class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordOneChar = {}
        wordTwoChar = {} 

        if len(s) != len(t):
            return False
        
        for charI, charO in zip(s, t):
            if charI in wordOneChar: 
                wordOneChar[charI] += 1
            else: 
                wordOneChar[charI] = 1
            
            if charO in wordTwoChar: 
                wordTwoChar[charO] += 1
            else: 
                wordTwoChar[charO] = 1

        print(wordOneChar)
        print(wordTwoChar)

        if wordOneChar == wordTwoChar: 
            return True

        return False 
            
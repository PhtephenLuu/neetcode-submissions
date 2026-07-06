class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(0, len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr not in anagrams: 
                anagrams[sortedStr] = [strs[i]]
            else:
                anagrams[sortedStr].append(strs[i])
        
        return list(anagrams.values())

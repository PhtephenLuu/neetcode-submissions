class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(0, len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr not in anagrams: 
                anagrams[sortedStr] = [i]
            else:
                anagrams[sortedStr].append(i)
        
        return [
            [strs[idx] for idx in indices] 
            for indices in anagrams.values()
        ]

class Solution:
    '''
    Concat each word into a encoded string and have some sort of decorator between words
    ["hello", "world"] -> "hello/world" 
    Decode: 
    Break up strings by the decorator in this case "/" 
    "hello/world" -> ["hello", "world"]
    '''

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '🫥'
        return '😀'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == '🫥':
            return []
        if s == '':
            return ['']
        return s.split('😀')

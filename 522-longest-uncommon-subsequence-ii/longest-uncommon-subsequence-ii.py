class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(a, b):
            
            it = iter(b)
            return all(c in it for c in a)
        
        strs.sort(key=len, reverse=True)  
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)
        return -1 
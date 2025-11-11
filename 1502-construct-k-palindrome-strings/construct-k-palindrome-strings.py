class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        count = Counter(s)
        odd = sum(v % 2 for v in count.values())
        
        return odd <= k

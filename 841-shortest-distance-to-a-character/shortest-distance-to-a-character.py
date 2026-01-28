class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = []
        prev = -n

        # from left to right
        for i in range(n):
            if s[i] == c:
                prev = i
            v = i - prev
            ans.append(v)
        
        # from right to left
        prev = 2 * n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                prev = i
            v = prev - i
            min_val = min(v, ans[i])
            ans[i] = min_val
        return ans 




        
        
        
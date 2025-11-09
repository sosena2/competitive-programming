class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
       
        def ways(m: int) -> int:
            if m < 0:
                return 0
            return math.comb(m + 2, 2)
        
        if n > 3 * limit:
            return 0
        
        L = limit + 1
        ans = (
            ways(n)
            - 3 * ways(n - L)
            + 3 * ways(n - 2 * L)
            - ways(n - 3 * L)
        )
        
        return ans 
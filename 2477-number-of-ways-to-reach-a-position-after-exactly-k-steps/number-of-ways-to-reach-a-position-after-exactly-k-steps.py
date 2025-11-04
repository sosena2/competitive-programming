class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # top down
        memo = {}
        mod = 10**9 + 7
        def ways(val, steps):
            if steps ==0:
                if val == endPos:
                    return  1
                else:
                    return 0
            if (val, steps) not in memo:
                # right
                right = ways (val + 1, steps - 1)
                # left
                left = ways( val - 1, steps - 1)
                memo[(val, steps)] = right + left
            return memo[(val, steps)]

        return ways(startPos, k) % mod
            
        
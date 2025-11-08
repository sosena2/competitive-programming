class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        
        memo = {}

        def dfs(used: int, total: int) -> bool:
            if used in memo:
                return memo[used]
            for i in range(maxChoosableInteger):
                if not (used >> i) & 1:  
                    if total + i + 1 >= desiredTotal or not dfs(used | (1 << i), total + i + 1):
                        memo[used] = True
                        return True
            memo[used] = False
            return False
        
        return dfs(0, 0)
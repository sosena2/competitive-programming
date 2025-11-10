class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        
        for step in range(k):
            dp2 = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                dp2[nr][nc] += dp[r][c] / 8
            dp = dp2
        return sum(map(sum, dp))

class Solution:
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Only store dp for the current row
        dp = [[0] * k for _ in range(n)]
        
        # Initialize first cell
        dp[0][grid[0][0] % k] = 1
        
        # Fill first row
        for j in range(1, n):
            new_dp = [0] * k
            for r in range(k):
                if dp[j-1][r] > 0:
                    new_r = (r + grid[0][j]) % k
                    new_dp[new_r] = (new_dp[new_r] + dp[j-1][r]) % MOD
            dp[j] = new_dp
        
        # Fill remaining rows
        for i in range(1, m):
            new_row = [[0] * k for _ in range(n)]
            
            # First column of each row
            for r in range(k):
                if dp[0][r] > 0:
                    new_r = (r + grid[i][0]) % k
                    new_row[0][new_r] = (new_row[0][new_r] + dp[0][r]) % MOD
            
            # Fill rest of row
            for j in range(1, n):
                for r in range(k):
                    # From top
                    if dp[j][r] > 0:
                        new_r = (r + grid[i][j]) % k
                        new_row[j][new_r] = (new_row[j][new_r] + dp[j][r]) % MOD
                    
                    # From left
                    if new_row[j-1][r] > 0:
                        new_r = (r + grid[i][j]) % k
                        new_row[j][new_r] = (new_row[j][new_r] + new_row[j-1][r]) % MOD
            
            dp = new_row
        
        # Result = number of paths ending where remainder is 0
        return dp[-1][0] % MOD

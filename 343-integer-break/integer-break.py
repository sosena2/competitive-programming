class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1  

        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 3

        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])

        return dp[n]
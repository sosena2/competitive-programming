class Solution:
    def numSquares(self, n: int) -> int:
        # creating an array of perfect square
        perfect = []
        for i in range(1,n+1):
            square = i*i
            if square <= n:
                perfect.append(square)

        dp = [inf] * (n +1)
        dp[0] = 0
        for target in range(n+1):
            for p in perfect:
                if  target >= p:
                    dp[target] = min(dp[target], dp[target - p] + 1)
        
        ans = dp[n]
        return ans

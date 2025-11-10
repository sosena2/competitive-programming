class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

    
        dp = [[0] * 2 for _ in range(k + 1)]
        for t in range(1, k + 1):
            dp[t][1] = -prices[0]  

        for price in prices[1:]:
            for t in range(1, k + 1):
                dp[t][0] = max(dp[t][0], dp[t][1] + price)       
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)     

        return dp[k][0]
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buttom up
        # the recurrence depends on the current day and ability to buy
        n = len(prices)
        dp = [[0]*2 for _ in range(n + 1)]
    
        # last day no profit possible
        dp[n][0] = dp[n][1] = 0

        for idx in range(n-1, -1, -1):
           
            # recurrence relation
            dp[idx][1] = max(dp[idx+1][0] - prices[idx], dp[idx+1][1])
            dp[idx][0] = max(dp[idx+1][1] + prices[idx] - fee, dp[idx+1][0])

        return dp[0][1]


            

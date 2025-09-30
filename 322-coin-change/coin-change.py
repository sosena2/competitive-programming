class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # buttom up dp
        dp = [inf]*(amount + 1)
        dp[0] = 0
        for target in range(amount + 1):
            for coin in coins:
                if target >= coin:
                    dp[target] = min(dp[target], dp[target-coin]+1)
        ans = dp[amount]
        return ans if ans != inf else -1


            
            

            

        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount+1)
        dp[0] = 0

        for rem_amount in range(1, amount + 1):
            for coin in coins:
                if rem_amount >= coin:
                    dp[rem_amount] = min(dp[rem_amount], dp[rem_amount - coin] + 1)
        ans = dp[amount]
        
        if ans == inf: ans = -1
        return ans

            
            

            

        